from Deque_Generator import get_deque

class Queue:

  def __init__(self):
    self.__dq = get_deque()
    self.__size = 0

  def __str__(self):
    # TODO replace pass with your implementation.
    # Orient your string from front (left) to back (right).
    return str(self.__dq)

  def __len__(self):
    # TODO replace pass with your implementation.
    return self.__size

  def enqueue(self, val):
    self.__dq.push_back(val)
    self.__size+=1

  def dequeue(self):
    if self.__size==0:
      
      
      return None
    x=self.__dq.pop_front()
    self.__size-=1
    return x

  def peek(self):
    if self.__size==0:
      return None
    x=self.__dq.peek_front()
    return x

#Unit tests make the main section unneccessary.
if __name__ == '__main__':
  x=Queue()
  x.enqueue(8)
  x.enqueue(-7)
  print(x.dequeue())
  print(x)
  
