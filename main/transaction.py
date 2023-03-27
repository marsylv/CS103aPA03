import sqlite3


# Marsyl
def to_dict(t):
    ''' t is a tuple  item_num, amount, category, date, description)'''
    transaction = { 'item_num': t[0], 'amount': t[1], 'category': t[2], 'date': t[3], 'description': t[4]}
    return transaction

dbFile = ""
class Transaction():
    # Marsyl
    def __init__(self):
        self.db_file = "transactions"
        self.run_query('''CREATE TABLE IF NOT EXISTS transactions
                           item_num integer primary key autoincrement,
                           amount real,
                           category text,
                           date text,
                           description text)''')

    # Marsyl
    def select_all(self):
        ''' return all transactions as a list of dicts.'''
        return self.run_query("SELECT * from transactions",())

    # Marsyl
    def select_by_category(self, category):
        ''' return all transactions with given category as a list of dicts.'''
        return self.run_query("SELECT * from transactions WHERE category=?", (category,))

    # Nathan
    def add_category(self, column, type):
        return self.run_query("ALTER TABLE transactions ADD COLUMN {column} {type}")

    # Nathan
    def show_categories(self):
        con = sqlite3.connect(self.dbFile)
        cur = con.cursor()
        cur.execute("SELECT * FROM transaction LIMIT 0")
        columns = [col[0] for col in cur.description]
        con.close()

        return columns
    
    def modify_category(self, old_column, new_column):
        con = sqlite3.connect(self.dbFile)
        cur = con.cursor()
        cur.execute("ALTER TABLE transactions RENAME COLUMN {old_column} TO {new_column}")
        con.close()
        return
    
    # Marsyl 
    def add(self, transaction):
        ''' create a transaction and add it to the transactions table '''
        return self.run_query("INSERT INTO transactions (amount, category, date, description) VALUES(?,?,?,?)",
                              (transaction['amount'], transaction['category'], transaction['date'], transaction['description']))

    # Marsyl
    def delete(self, item_num):
        ''' delete a transaction '''
        return self.run_query("DELETE FROM transactions WHERE item_num=?",  item_num,))

    # Marsyl
    def update(self, item_num, field, new_value):
       # ''' update a transaction's field '''
        return self.run_query(f"UPDATE transactions SET {field}=? WHERE item_num=?", (new_value, item_num))

    # Marsyl
    def sum_by_date(self):
        #''' return sum of all transactions grouped by date '''
        return self.run_query("SELECT date, SUM(amount) FROM transactions GROUP BY date",())

    # Marsyl
    def sum_by_month(self):
        ''' return sum of all transactions grouped by month '''
        return self.run_query("SELECT strftime('%Y-%m',date) as month, SUM(amount) FROM transactions GROUP BY month",())
     # Marsyl
    def sum_by_year(self):
        #''' return sum of all transactions grouped by year '''
        return self.run_query("SELECT strftime('%Y',date) as year, SUM(amount) FROM transactions GROUP BY year",())

    # Marsyl
    def run_query(self, query):
        #''' execute a SQL query and return the result as a list of dicts.'''
        con = sqlite3.connect(self.db_file)
        cur = con.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        con.commit()
        con.close()
        return [to_dict(row) for row in rows]
