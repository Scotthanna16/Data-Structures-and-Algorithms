from Stack import Stack
import sys # for sys.argv, the command-line arguments

def delimiter_check(filename):
  stack=Stack()
  with open(filename,'r') as file:
    contents=file.read()
    for x in range(len(contents)):
      if contents[x:x+1] == '(' or contents[x:x+1] == '[' or contents[x:x+1] == '{' or contents[x:x+1] == '}' or contents[x:x+1] == ']' or contents[x:x+1] == ')':
        
        if contents[x:x+1] == '(' or contents[x:x+1] == '[' or contents[x:x+1] == '{':
          stack.push(contents[x:x+1])
          
          
        else:
          if (stack.peek() == '[' and contents[x:x+1]==']') or  (stack.peek() == '(' and contents[x:x+1]==')') or (stack.peek() == '{' and contents[x:x+1]=='}'):
            stack.pop()
          else:
            return False
    if len(stack)==0:
      return True
    else:
      return False


   

  

if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command 
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_check.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_check.py']
  if len(sys.argv) < 2:
    # This means the user did not provide the filename to check.
    # Show the correct usage.
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')

