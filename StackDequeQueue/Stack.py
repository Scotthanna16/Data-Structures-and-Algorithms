from Deque_Generator import get_deque

class Stack:

  def __init__(self):
    self.__dq = get_deque()
    self.__size=0

  def __str__(self):
    # TODO replace pass with your implementation.
    # Orient your string from top (left) to bottom (right).
   
    return str(self.__dq)

  def __len__(self):
    # TODO replace pass with your implementation.
    return self.__size

  def push(self, val):
    self.__dq.push_front(val)
    self.__size+=1

  def pop(self):
    if self.__size==0:
      
      return None
    x=self.__dq.pop_front()
    self.__size-=1
    return x

  def peek(self):
    x=self.__dq.peek_front()
    return x 
   

# Unit tests make the main section unneccessary.
if __name__ == '__main__':
  x = Stack()
  x.push(3)
  x.push(5)
  x.pop()
  x.pop()
  x.push(7)
  print(x.peek())
  print(x.pop())
  print(x)