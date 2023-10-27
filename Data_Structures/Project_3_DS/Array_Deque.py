
from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
   
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    self.__FI=0
    self.__BI=0
    self.__size=0

    pass
    
  def __str__(self):
    # TODO replace pass with an implementation that returns a string of
    # exactly the same format as the __str__ method in the Linked_List_Deque.
    # Orient your string from front (left) to back (right).
   
    
  
    if self.__size==0:
      return('[ ]')
    elif self.__size==1:
      return('[ '+str(self.__contents[self.__FI])+' ]')
    else:
      string =''
    #The array is good, front and back work, just the printing is wrong 
      if self.__FI>self.__BI:
        q=[]
        y=[]
        for x in range(self.__capacity-self.__FI):
          q+=[self.__contents[self.__FI +x]]
        for x in range (0,int(self.__BI)+1):
          y+=[self.__contents[x]]
        z=q+y
        for l in range(len(z)-1):
          string = string +str(z[l]) +', '
        return '[ '+string+ str(z[len(z)-1])+' ]'
      else:
        t=[]
        for x in range(0,int(self.__BI) -self.__FI+1):
          t+=[self.__contents[self.__FI +x]]
        for l in range(len(t)-1):
          string = string +str(t[l]) +', '
        return '[ '+string+ str(t[len(t)-1])+' ]'
        


        



    
   
    
  def __len__(self):
    # TODO replace pass with an implementation that returns the number of
    # items in the deque. This method must run in constant time.
    return self.__size

  def __grow(self):
    new_array=2*len(self.__contents)*[None]
    
   
    if self.__FI>self.__BI:
    
   
      for x in range(len(self.__contents)):
        new_array[x]=self.__contents[(self.__FI +x)%self.__size]
        
      
    elif self.__FI==self.__BI:
      
      new_array[0]=self.__contents[0]
     
    else:
      for x in range(self.__size):
        new_array[x]=self.__contents[x]
        
       
    self.__contents=new_array
    
    self.__capacity*=2
    self.__FI=0
    self.__BI=self.__capacity/2-1

        


    
  def push_front(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    
    if self.__size==self.__capacity:
      self.__grow()
    if self.__size==0:
      self.__contents=[val]
      self.__size=1
      return
    if self.__capacity ==1:
      self.__contents[0]=val
      self.__size=1
    
    else:
      if self.__FI==0:
        self.__size+=1
        
        self.__contents[self.__capacity-1]=val

        self.__FI=self.__capacity-1
      else:
        self.__contents[self.__FI-1]=val
        self.__FI-=1
        self.__size+=1
       
    
  def push_back(self, val):
    if self.__size==self.__capacity:
      self.__grow() 
    if self.__size==0:
      self.__contents=[val]
      self.__size=1
      return
    if self.__capacity ==1:
      self.__contents[0]=val
      self.__size=1
   
    else:
      if self.__BI==self.__capacity:
        self.__size+=1
        self.__contents[0]=val
        self.__BI=1
         
      else:
        self.__contents[int(self.__BI)+1]=val
        self.__BI+=1
        self.__size+=1



    
  def pop_front(self):
    if self.__size==0:
      self.__size==0
      return None
    elif self.__BI==0 and self.__FI ==0:
      x=self.__contents[int(self.__FI)]
      self.__contents=[None]
      self.__capacity=1
      self.__size=0
      return x
    elif self.__BI==self.__FI:
      x=self.__contents[int(self.__FI)]
      self.__contents=[None]
      self.__BI=0
      self.__FI=0
      self.__size=0
      self.__capacity=1
      return x
    elif self.__FI==self.__capacity-1:
      
      x=self.__contents[int(self.__FI)]
      self.__FI=0
      self.__size-=1
      if self.__size==0:
        self.__contents=[]
      return x
    else:
      x=self.__contents[int(self.__FI)]
      self.__FI+=1
      self.__size -=1
      if self.__size==0:
        self.__contents=[]
      return x
    

    
  def peek_front(self):
    if self.__size==0:
      return None
    return self.__contents[self.__FI]
    
 
      
  
  def pop_back(self):
    if self.__size==0:
      self.__size==0
      return None
    elif self.__BI==0 and self.__FI ==0:
      x=self.__contents[int(self.__BI)]
      self.__contents=[None]
      self.__capacity=1
      self.__size=0
      return x
    elif self.__BI==self.__FI:
      x=self.__contents[int(self.__FI)]
      self.__contents=[None]
      self.__BI=0
      self.__FI=0
      self.__size=0
      self.__capacity=1
      return x
    elif self.__BI==0:
      x=self.__contents[int(self.__BI)]
      self.__BI=self.__capacity-1
      self.__size-=1
      if self.__size==0:
        self.__contents=[]
      return x
    else:
      x=self.__contents[int(self.__BI)]
      self.__BI-=1
      self.__size-=1
      if self.__size==0:
        self.__contents=[]
      return x
    




  def peek_back(self):
    if self.__size==0:
      
      
      return None
    return self.__contents[int(self.__BI)]

# No main section is necessary. Unit tests take its place.
if __name__ == '__main__':
  x=Array_Deque()
  
  x.push_front(8)
  
  x.push_front(7)
  x.push_front(6)
  
  x.push_front(5)
  
 
 
  x.pop_front()
  
  x.pop_front()
  x.pop_front()
  
  x.pop_front()

  x.push_front(1)
  x.push_front(2)
  print(x)
  
  


  
 
