import sqlite3

def toDict(t):
    ''' t is a tuple (item_number, amount, category, date, description)'''
    transaction = {'item_number': t[0], 'amount': t[1], 'category': t[2], 'date': t[3], 'description': t[4]}
    return transaction

class Transaction():
    def __init__(self, dbFile):
        self.dbFile = dbFile
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions
                          (item_number integer primary key autoincrement,
                           amount real,
                           category text,
                           date text,
                           description text)''')

    def selectAll(self):
        ''' return all transactions as a list of dicts.'''
        return self.runQuery("SELECT * from transactions",())

    def selectByCategory(self, category):
        ''' return all transactions with given category as a list of dicts.'''
        return self.runQuery("SELECT * from transactions WHERE category=?", (category,))

    def add(self, transaction):
        ''' create a transaction and add it to the transactions table '''
        return self.runQuery("INSERT INTO transactions (amount, category, date, description) VALUES(?,?,?,?)",
                              (transaction['amount'], transaction['category'], transaction['date'], transaction['description']))

    def delete(self, item_number):
        ''' delete a transaction '''
        return self.runQuery("DELETE FROM transactions WHERE item_number=?", (item_number,))

    def update(self, item_number, field, new_value):
        ''' update a transaction's field '''
        return self.runQuery(f"UPDATE transactions SET {field}=? WHERE item_number=?", (new_value, item_number))

    def sumByDate(self):
        ''' return sum of all transactions grouped by date '''
        return self.runQuery("SELECT date, SUM(amount) FROM transactions GROUP BY date",())

    def sumByMonth(self):
        ''' return sum of all transactions grouped by month '''
        return self.runQuery("SELECT strftime('%Y-%m',date) as month, SUM(amount) FROM transactions GROUP BY month",())

    def sumByYear(self):
        ''' return sum of all transactions grouped by year '''
        return self.runQuery("SELECT strftime('%Y',date) as year, SUM(amount) FROM transactions GROUP BY year",())

    def runQuery(self, query, params):
        ''' execute a SQL query and return the result as a list of dicts.'''
        con = sqlite3.connect(self.dbFile)
        cur = con.cursor()
        cur.execute(query, params)
        rows = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(row) for row in rows]
