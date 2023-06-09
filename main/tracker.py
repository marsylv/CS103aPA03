from transaction import Transaction

def main():
    while (True):
      prompt = input("Enter command:\n")
      prompt = prompt.strip()

      if prompt == "quit":
          print("Exiting the program now!")
          break
      
      process_args(prompt.split())

# Alex
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

# Alex
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

    elif len(arglist) == 4 and arglist[0]=="summarize" and arglist[1]=="transactions" and arglist[2]=="by":
        if arglist[3] == "date":
            print(transactions.sumByDate())
        elif arglist[3] == "month":
            print(transactions.sumByMonth())
        elif arglist[3] == "month":
            print(transactions.sumByYear())
        elif arglist[3] == "category":
            print(transactions.selectByCategory())
    
    elif arglist[0]=='delete':
        if len(arglist)!= 3:
            print_usage()
        else:
            if arglist[1] == "transaction":
                transactions.delete(arglist[2])
            
    print(arglist," is not implemented.")
    print_usage()
main()