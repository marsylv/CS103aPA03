from transaction import Transaction
import sys

def main():
    while (True):
      prompt = input("Enter command:\n")
      prompt = prompt.trim()

      process_args(prompt)

      if prompt == "quit":
          break

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
    ''' examine args and make appropriate calls to TodoList'''
    transactions = Transaction()
    if arglist==[]:
        print_usage()
    elif arglist[0]=="show":
        print_todos(todolist.selectActive())
    elif arglist[0]=="showall":
        print_todos(todos = todolist.selectAll())
    elif arglist[0]=="showcomplete":
        print_todos(todolist.selectCompleted())
    elif arglist[0]=='add':
        if len(arglist)!=3:
            print_usage()
        else:
            todo = {'title':arglist[1],'desc':arglist[2],'completed':0}
            todolist.add(todo)
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