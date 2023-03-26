from transaction import Transaction
import sys

def main():
    while (True):
      prompt = input("Enter command:\n")
      prompt = prompt.trim()

      if prompt == "quit":
          break
      
      process_args(prompt.split())


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
        else:
            todo = {'title':arglist[1],'desc':arglist[2],'completed':0}
            todolist.add(todo)
    elif len(arglist) == 4 && arglist[0]=="summarize" && arglist[1]=="transactions" && arglist[2]=="by":
        if arglist[3] == "date":
            print(transactions.sumByDate())
        elif arglist[3] == "month":
            print(transactions.sumByMonth())
        elif arglist[3] == "month":
            print(transactions.sumByYear())
        elif arglist[3] == "category":
            print(transactions.selectByCategory())
    
    elif arglist[0]=='delete':
        if len(arglist)!= 2:
            print_usage()
        else:
            todolist.delete(arglist[1])
    else:
        print(arglist,"is not implemented")
        print_usage()


main()