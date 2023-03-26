from transaction import Transaction
import sys

def main():
    while (True):
      prompt = input("Enter command:\n")
      prompt = prompt.trim()

      if prompt == "quit":
          break
      
      process_args(prompt)


def print_usage():
    print('''usage:
      quit
      show categories
      add category
      modify category
      show transactions
      add transaction
      delete transaction
      summarize transactions by date
      summarize transactions by month
      summarize transactions by year
      summarize transactions by category
      ''')
    
def process_args(arglist):
    ''' examine args and make appropriate calls to transaction database'''
    transactions = Transaction()
    if arglist==[]:
        print_usage()
    elif arglist[0]=="show":
        if len(arglist) != 2:
            print_usage()
        elif arglist[1] == "categories":
            print(transactions.show_categories())
        elif arglist[1] == "transactions":
            print(transactions.selectAll())
    elif arglist[0]=='add':
        if len(arglist)!=3:
            print_usage()
        elif arglist[1] == "category":
            try:
                print(transactions.add_category(arglist[2]))
            except:
                print("Invalid Category")
        elif arglist[1] == "transaction":
            try:
                print(transactions.add(arglist[2]))
            except:
                print("Invalid transaction")
    elif arglist[0]=='complete':
        if len(arglist)!= 2:
            print_usage()
        else:
            todolist.setComplete(arglist[1])
    elif arglist[0]=='delete':
        if len(arglist)!= 2:
            print_usage()
        else:
            todolist.delete(arglist[1])
    else:
        print(arglist,"is not implemented")
        print_usage()


main()