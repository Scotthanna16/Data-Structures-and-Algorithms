import timeit
from Stack import Stack

def Hanoi_rec(n, s, a,d):
  print(n, s, d, a)
  # TODO replace pass with your base and recursive cases.
  if n ==0:
    a.push(s.pop())
    print(n,s,d,a)
    print()
    return
  else:
    Hanoi_rec(n-1,s,d,a)
    a.push(s.pop())
    Hanoi_rec(n-1,d,a,s)
   
  
  print(n, s, d, a)
  print()

def Hanoi(n):
  source = Stack()
  dest = Stack()
  aux = Stack()
  i = n-1
  while i >= 0:
    source.push(i)
    i = i - 1
  Hanoi_rec(n-1, source, aux, dest)

if __name__ == "__main__":
  n=19
  runtime = timeit.timeit("Hanoi(n)", setup="from __main__ import Hanoi,n", number=1)
  print("computed Hanoi(" + str(n) + ") in " + str(runtime) + " seconds.")
