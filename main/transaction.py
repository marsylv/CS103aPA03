import sqlite3

# Marsyl
def toDict(t):
    ''' t is a tuple (itemNum, amount, category, date, description)'''
    transaction = {'itemNum': t[0], 'amount': t[1], 'category': t[2], 'date': t[3], 'description': t[4]}
    return transaction

class Transaction():
    # Marsyl
    def __init__(self, dbFile):
        self.dbFile = dbFile
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions
                          (itemNum integer primary key autoincrement,
                           amount real,
                           category text,
                           date text,
                           description text)''')

    # Marsyl
    def selectAll(self):
        ''' return all transactions as a list of dicts.'''
        return self.runQuery("SELECT * from transactions",())

    # Marsyl
    def selectByCategory(self, category):
        ''' return all transactions with given category as a list of dicts.'''
        return self.runQuery("SELECT * from transactions WHERE category=?", (category,))

    # Nathan
    def add_category(self, column, type):
        return self.runQuery("ALTER TABLE transactions ADD COLUMN {column} {type}")

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
        return self.runQuery("INSERT INTO transactions (amount, category, date, description) VALUES(?,?,?,?)",
                              (transaction['amount'], transaction['category'], transaction['date'], transaction['description']))

    # Marsyl
    def delete(self, itemNum):
        ''' delete a transaction '''
        return self.runQuery("DELETE FROM transactions WHERE itemNum=?", (itemNum))

    # Marsyl
    def update(self, itemNum, field, new_value):
        ''' update a transaction's field '''
        return self.runQuery(f"UPDATE transactions SET {field}=? WHERE itemNum=?", (new_value, itemNum))

    # Marsyl
    def sumByDate(self):
        ''' return sum of all transactions grouped by date '''
        return self.runQuery("SELECT date, SUM(amount) FROM transactions GROUP BY date",())

    # Marsyl
    def sumByMonth(self):
        ''' return sum of all transactions grouped by month '''
        return self.runQuery("SELECT strftime('%Y-%m',date) as month, SUM(amount) FROM transactions GROUP BY month",())
     # Marsyl
    def sumByYear(self):
        ''' return sum of all transactions grouped by year '''
        return self.runQuery("SELECT strftime('%Y',date) as year, SUM(amount) FROM transactions GROUP BY year",())

    # Marsyl
    def runQuery(self, query, params):
        ''' execute a SQL query and return the result as a list of dicts.'''
        con = sqlite3.connect(self.dbFile)
        cur = con.cursor()
        cur.execute(query, params)
        rows = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(row) for row in rows]
