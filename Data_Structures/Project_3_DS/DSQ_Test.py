import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    self.__deque = get_deque(0)
    self.__stack = Stack()
    self.__queue = Queue()
  


  



  def test_empty_deque(self):
    self.assertEqual('[ ]', str(self.__deque), 'Empty deque should print as "[ ]"')
  def test_emptydequelen(self):
    x=self.__deque
    self.assertEqual(len(x),0)
  def test_popbemptydeque(self):
    x=self.__deque
    y=x.pop_back()
    self.assertEqual(None,y)
  def test_popfemptydequelen(self):
    x=self.__deque.pop_front()
    self.assertEqual(len(self.__deque),0)
  
  def test_popbemptydequelen(self):
    x=self.__deque.pop_back()
    self.assertEqual(len(self.__deque),0)
  def test_popfemptydeque(self):
    x=self.__deque
    y=x.pop_front()
    self.assertEqual(None,y)
  def test_peekfemptydeque(self):
    x=self.__deque
    y=x.peek_front()
    self.assertEqual(None,y)
  def test_peekbemptydeque(self):
    x=self.__deque
    y=x.peek_back()
    self.assertEqual(None,y)
    
  def test_peekfemptydequeoutput(self):
    self.__deque.peek_front()

    self.assertEqual(str(self.__deque),'[ ]')
  def test_peekbemptydequeoutput(self):
    self.__deque.peek_back()
    self.assertEqual(str(self.__deque),'[ ]')
 
  def test_popbemptydequeoutput(self):
    self.__deque.pop_back()
    self.assertEqual(str(self.__deque),'[ ]')
  def test_popfemptydequeoutput(self):
    self.__deque.pop_front()
    self.assertEqual(str(self.__deque),'[ ]')
  
  def test_pushf_deque(self):
    self.__deque.push_front(7)
    self.assertEqual('[ 7 ]', str(self.__deque))
  def test_3pushf_deque(self):
    self.__deque.push_front(7)
    self.__deque.push_front(3)
    self.__deque.push_front(6)
    self.assertEqual('[ 6, 3, 7 ]', str(self.__deque))
  def test_pushb_deque(self):
    self.__deque.push_back(7)
    self.assertEqual('[ 7 ]', str(self.__deque))
  def test_3pushb_deque(self):
    self.__deque.push_back(7)
    self.__deque.push_back(3)
    self.__deque.push_back(6)
    self.assertEqual('[ 7, 3, 6 ]', str(self.__deque))
  def test_1pushf2pushb_deque(self):
    self.__deque.push_front(7)
    self.__deque.push_back(3)
    self.__deque.push_back(6)
    self.assertEqual('[ 7, 3, 6 ]', str(self.__deque))
  def test_2pushf1pushb_deque(self):
    self.__deque.push_front(7)
    self.__deque.push_front(3)
    self.__deque.push_back(6)
    self.assertEqual('[ 3, 7, 6 ]', str(self.__deque))
  def test_1pf1pushb1pf_deque(self):
    self.__deque.push_front(7)
    self.__deque.push_back(3)
    self.__deque.push_front(6)
    self.assertEqual('[ 6, 7, 3 ]', str(self.__deque))
  def test_1pushf1popf_deque(self):
    self.__deque.push_front(7)
    self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))
  def test_1pushf1popb_deque(self):
    self.__deque.push_front(7)
    self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))
  def test_1pushb1popf_deque(self):
    self.__deque.push_back(7)
    self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))
  def test_1pushb1popb_deque(self):
    self.__deque.push_back(7)
    self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))
  
  def test_2pushf2popf_deque(self):
    self.__deque.push_front(7)
    self.__deque.pop_front()
    self.__deque.push_front(7)
    self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))
  def test_2pushf2popb_deque(self):
    self.__deque.push_front(7)
    self.__deque.pop_back()
    self.__deque.push_front(7)
    self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))
  def test_2pushb2popf_deque(self):
    self.__deque.push_back(7)
    self.__deque.pop_front()
    self.__deque.push_back(7)
    self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))
  def test_2pushb2popb_deque(self):
    self.__deque.push_back(7)
    self.__deque.pop_back()
    self.__deque.push_back(7)
    self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))

  def test_2pushf2popf_dequelen(self):
    self.__deque.push_front(7)
    self.__deque.pop_front()
    self.__deque.push_front(7)
    self.__deque.pop_front()
    self.assertEqual(len(self.__deque),0)
  def test_2pushf2popb_dequelen(self):
    self.__deque.push_front(7)
    self.__deque.pop_back()
    self.__deque.push_front(7)
    self.__deque.pop_back()
    self.assertEqual(len(self.__deque),0)
  def test_2pushb2popf_dequelen(self):
    self.__deque.push_back(7)
    self.__deque.pop_front()
    self.__deque.push_back(7)
    self.__deque.pop_front()
    self.assertEqual(len(self.__deque),0)
  def test_2pushb2popb_dequelen(self):
    self.__deque.push_back(7)
    self.__deque.pop_back()
    self.__deque.push_back(7)
    self.__deque.pop_back()
    self.assertEqual(len(self.__deque),0)
  def test_2pushf1popf_dequelen(self):
    self.__deque.push_front(7)
    self.__deque.pop_front()
    self.__deque.push_front(7)
   
    self.assertEqual(len(self.__deque),1)
  def test_2pushf1popb_dequelen(self):
    self.__deque.push_front(7)
    self.__deque.pop_back()
    self.__deque.push_front(7)
   
    self.assertEqual(len(self.__deque),1)
  def test_2pushb1popf_dequelen(self):
    self.__deque.push_back(7)
    self.__deque.pop_front()
    self.__deque.push_back(7)
   
    self.assertEqual(len(self.__deque),1)
  def test_2pushb1popb_dequelen(self):
    self.__deque.push_back(7)
    self.__deque.pop_back()
    self.__deque.push_back(7)   
    self.assertEqual(len(self.__deque),1)
  def test_2pushf1popf_dequeval(self):
    self.__deque.push_front(7)
    self.__deque.pop_front()
    self.__deque.push_front(5)
    x=self.__deque.pop_front()
    self.assertEqual(x,5)
  def test_2pushf2popb_dequeval(self):
    self.__deque.push_front(7)
    self.__deque.pop_back()
    self.__deque.push_front(5)
    x=self.__deque.pop_back()
    self.assertEqual(x,5)
  def test_2pushb2popf_dequeval(self):
    self.__deque.push_back(7)
    self.__deque.pop_front()
    self.__deque.push_back(5)
    x=self.__deque.pop_front()
    self.assertEqual(x,5)
  def test_2pushb2popb_dequeval(self):
    self.__deque.push_back(7)
    self.__deque.pop_back()
    self.__deque.push_back(5)
    x=self.__deque.pop_back()
    self.assertEqual(x,5)
  
  def test_2pushf1peekf_deque(self):
    self.__deque.push_front(7)
    self.__deque.push_front(5)
    x = self.__deque.peek_front()
    self.assertEqual(5, x)
    
  def test_2pushb1peakf_deque(self):
    self.__deque.push_back(7)
    
    self.__deque.push_back(5)
    x= self.__deque.peek_front()
    self.assertEqual(7,x)
  def test_2pushb1peekb_deque(self):
    self.__deque.push_back(7)
    
    self.__deque.push_back(5)
    x= self.__deque.peek_back()
    self.assertEqual(5,x)
    
  def test_2pushf1peekb_deque(self):
    self.__deque.push_front(7)
    
    self.__deque.push_front(5)
    x= self.__deque.peek_back()
    self.assertEqual(7,x)

  def test_pushf1lendeque(self):
    self.__deque.push_front(7)
    self.assertEqual(1,len(self.__deque))
  def test_pushb1valdeque(self):
    self.__deque.push_back(7)
    self.assertEqual(1,len(self.__deque))

  def test_2pushf1peekf_dequelen(self):
    self.__deque.push_front(7)
    self.__deque.push_front(5)
    self.__deque.peek_front()
    self.assertEqual(len(self.__deque), 2)
    
  def test_2pushb1peakf_dequelen(self):
    self.__deque.push_back(7)
    
    self.__deque.push_back(5)
    self.__deque.peek_front()
    self.assertEqual(len(self.__deque), 2)
  def test_2pushb1peekb_dequelen(self):
    self.__deque.push_back(7)
    
    self.__deque.push_back(5)
    self.__deque.peek_back()
    self.assertEqual(len(self.__deque), 2)
    
  def test_2pushf1peekb_dequelen(self):
    self.__deque.push_front(7)
    
    self.__deque.push_front(5)
    self.__deque.peek_back()
    self.assertEqual(len(self.__deque), 2)
  def test_2pushffordequeoutput(self):
    self.__deque.push_front(4)
    self.__deque.push_front(3)
    self.assertEqual('[ 3, 4 ]' , str(self.__deque))
  def test_2pushffordequelength(self):
    self.__deque.push_front(4)
    self.__deque.push_front(3)
    self.assertEqual( 2 , len(self.__deque))

  def test_2pushbfordequeoutput(self):
    self.__deque.push_back(4)
    self.__deque.push_back(3)
    self.assertEqual('[ 4, 3 ]' , str(self.__deque))
  def test_2pushbfordequelength(self):
    self.__deque.push_front(4)
    self.__deque.push_front(3)
    self.assertEqual( 2 , len(self.__deque))

  def test_1pushf1pushbfordequeoutput(self):
    self.__deque.push_front(4)
    self.__deque.push_back(3)
    self.assertEqual('[ 4, 3 ]' , str(self.__deque))
  def test_1pushf1pushbfordequelength(self):
    self.__deque.push_front(4)
    self.__deque.push_back(3)
    self.assertEqual( 2 , len(self.__deque))
  def test_1pushb1pushffordequeoutput(self):
    self.__deque.push_back(4)
    self.__deque.push_front(3)
    self.assertEqual('[ 3, 4 ]' , str(self.__deque))
  def test_1pushb1pushffordequelength(self):
    self.__deque.push_back(4)
    self.__deque.push_front(3)
    self.assertEqual( 2 , len(self.__deque))














































  def test_popbemptystacklen(self):
    x=self.__stack.pop()
    self.assertEqual(len(self.__stack),0)
  def test_popemptystack(self):
    x=self.__stack
    y=x.pop()
    self.assertEqual(None,y)
  def test_peekemptystack(self):
    x=self.__stack
    y=x.peek()
    self.assertEqual(None,y)
  def test_peekemptystackkoutput(self):
    x=self.__stack.peek()
    self.assertEqual(str(self.__stack),'[ ]')
  def test_popemptystackoutput(self):
    self.__stack.pop()
    self.assertEqual(str(self.__stack),'[ ]')
  def test_emptystacklen(self):
    x=self.__stack
    self.assertEqual(len(x),0)
  def test_empty_stack(self):
    self.assertEqual('[ ]', str(self.__stack), 'Empty stack should print as "[ ]"')
  def test_push1valstack(self):
    self.__stack.push(7)
    self.assertEqual(1,len(self.__stack))
  def test_pushpopstackoutput(self):
    self.__stack.push(5)
    self.__stack.pop()
    self.assertEqual(str(self.__stack), '[ ]')
  def test_2push2popstackoutput(self):
    self.__stack.push(5)
    self.__stack.pop()
    self.__stack.push(5)
    self.__stack.pop()
    self.assertEqual(str(self.__stack), '[ ]')

  def test_2pushpopstackoutput(self):
    self.__stack.push(5)
    self.__stack.push(6)
    self.__stack.pop()
    self.assertEqual(str(self.__stack), '[ 5 ]')
  def test_2pushpopstacklen(self):
    self.__stack.push(5)
    self.__stack.pop()
    self.__stack.push(5)
    
    self.assertEqual(len(self.__stack), 1)

  def test_2pushstackoutput(self):
    self.__stack.push(5)
    self.__stack.push(6)
    self.assertEqual(str(self.__stack), '[ 6, 5 ]')
  def test_2pushplen(self):
    self.__stack.push(5)
    self.__stack.push(6)
    
    self.assertEqual(len(self.__stack), 2)
  
  def test_pushpopstacklen(self):
    self.__stack.push(5)
    self.__stack.pop()
    self.assertEqual(len(self.__stack), 0)
  def test_2push2popstacklen(self):
    self.__stack.push(5)
    self.__stack.pop()
    self.__stack.push(5)
    self.__stack.pop()
    self.assertEqual(len(self.__stack), 0)

  def test_pushpoppeekstacklen(self):
    self.__stack.push(5)
    self.__stack.pop()
    self.__stack.peek()
    self.assertEqual(len(self.__stack), 0)
  def test_pushpoppeekstackval(self):
    self.__stack.push(5)
    self.__stack.pop()
    x=self.__stack.peek()
    self.assertEqual(x, None)

  def test_pushpoppeekstackoutput(self):
    self.__stack.push(5)
    self.__stack.pop()
    self.__stack.peek()
    self.assertEqual('[ ]', str(self.__stack))

  def test_2pushpoppeekstacklen(self):
    self.__stack.push(5)
    self.__stack.push(5)
    self.__stack.pop()
    self.__stack.peek()
    self.assertEqual(len(self.__stack), 1)
  def test_2pushpoppeekstackval(self):
    self.__stack.push(5)
    self.__stack.push(5)
    self.__stack.pop()
    x=self.__stack.peek()
    self.assertEqual(x, 5)

  def test_2pushpoppeekstackoutput(self):
    self.__stack.push(5)
    self.__stack.push(5)
    self.__stack.pop()
    self.__stack.peek()
    self.assertEqual('[ 5 ]', str(self.__stack))
  def test_2pushpeekstackoutput(self):
    self.__stack.push(6)
    self.__stack.push(5)
    
    self.__stack.peek()
    self.assertEqual('[ 5, 6 ]', str(self.__stack))
  
  def test_2pushpeekstacklen(self):
    self.__stack.push(6)
    self.__stack.push(5)
    
    self.__stack.peek()
    self.assertEqual(2, len(self.__stack))
  
  def test_2pushpeekstackval(self):
    self.__stack.push(6)
    self.__stack.push(5)
    
    x=self.__stack.peek()
    self.assertEqual(5 , x)

  def test_3pushstackoutput(self):
    self.__stack.push(3)
    self.__stack.push(4)
    self.__stack.push(5)
    self.assertEqual('[ 5, 4, 3 ]' , str(self.__stack))

  def test_3pushstacklength(self):
    self.__stack.push(3)
    self.__stack.push(4)
    self.__stack.push(5)
    self.assertEqual( 3 , len(self.__stack))

  def test_3pushstackoutput1pop(self):
    self.__stack.push(3)
    self.__stack.push(4)
    self.__stack.push(5)
    self.__stack.pop()
    self.assertEqual('[ 4, 3 ]' , str(self.__stack))

  def test_3pushstacklength1pop(self):
    self.__stack.push(3)
    self.__stack.push(4)
    self.__stack.push(5)
    self.__stack.pop()
    self.assertEqual(2 , len(self.__stack))

  def test_3pushstackval1pop(self):
    self.__stack.push(3)
    self.__stack.push(4)
    self.__stack.push(5)
    x=self.__stack.pop()
    self.assertEqual( 5, x)

  def test_3pushstackval1peek(self):
    self.__stack.push(3)
    self.__stack.push(4)
    self.__stack.push(5)
    x=self.__stack.peek()
    self.assertEqual( 5, x)

  def test_3pushstackoutput2pop(self):
    self.__stack.push(3)
    self.__stack.push(4)
    self.__stack.push(5)
    self.__stack.pop()
    self.__stack.pop()
    self.assertEqual('[ 3 ]' , str(self.__stack))

  def test_3pushstacklength2pop(self):
    self.__stack.push(3)
    self.__stack.push(4)
    self.__stack.push(5)
    self.__stack.pop()
    self.__stack.pop()
    self.assertEqual(1 , len(self.__stack))

  def test_3pushstackval2pop(self):
    self.__stack.push(3)
    self.__stack.push(4)
    self.__stack.push(5)
    x=self.__stack.pop()
    x=self.__stack.pop()
    self.assertEqual(x, 4)

  def test_3pushstackoutput3pop(self):
    self.__stack.push(3)
    self.__stack.push(4)
    self.__stack.push(5)
    self.__stack.pop()
    self.__stack.pop()
    self.__stack.pop()
    self.assertEqual('[ ]' , str(self.__stack))

  def test_3pushstacklength3pop(self):
    self.__stack.push(3)
    self.__stack.push(4)
    self.__stack.push(5)
    self.__stack.pop()
    self.__stack.pop()
    self.__stack.pop()
    self.assertEqual(0 , len(self.__stack))

  def test_3pushstackval3pop(self):
    self.__stack.push(3)
    self.__stack.push(4)
    self.__stack.push(5)
    x=self.__stack.pop()
    x=self.__stack.pop()
    x=self.__stack.pop()
    self.assertEqual(x, 3)

  
  
  


  




















  def test_emptyquequelen(self):
    x=self.__queue
    self.assertEqual(len(x),0)
  def test_empty_queue(self):
    self.assertEqual('[ ]', str(self.__queue), 'Empty queue should print as "[ ]"')
  def test_dequeueemptyqueque(self):
    x=self.__queue
    y=x.dequeue()
    self.assertEqual(None,y)
  def test_peekemptyqueque(self):
    x=self.__queue
    y=x.peek()
    self.assertEqual(None,y)
  def test_emptyquequeoutputafterpeek(self):
    x=self.__queue.peek()
    self.assertEqual(str(self.__deque),'[ ]')
  def test_dequeueemptyquequeoutput(self):
    self.__queue.dequeue()
    self.assertEqual(str(self.__deque),'[ ]')
  def test_enqueue1val(self):
    self.__queue.enqueue(7)
    self.assertEqual(1,len(self.__queue))
  def test_endequeueoutput(self):
    self.__queue.enqueue(5)
    self.__queue.dequeue()
    self.assertEqual(str(self.__queue), '[ ]')
  def test_2endequeueoutput(self):
    self.__queue.enqueue(5)
    self.__queue.dequeue()
    self.__queue.enqueue(5)
    self.__queue.dequeue()
    self.assertEqual(str(self.__queue), '[ ]')

  def test_2en1dequeueoutput(self):
    self.__queue.enqueue(5)
    self.__queue.enqueue(7)
    self.__queue.dequeue()
    self.assertEqual(str(self.__queue), '[ 7 ]')
  def test_2en1deququqlen(self):
    self.__queue.enqueue(5)
    self.__queue.dequeue()
    self.__queue.enqueue(5)
    
    self.assertEqual(len(self.__queue), 1)

  def test_2enqueueoutput(self):
    self.__queue.enqueue(5)
    self.__queue.enqueue(7)
    self.assertEqual(str(self.__queue), '[ 5, 7 ]')
  def test_2enqueuelen(self):
    self.__queue.enqueue(5)
    self.__queue.enqueue(6)
    
    self.assertEqual(len(self.__queue), 2)
  
  def test_endequeuelen(self):
    self.__queue.enqueue(5)
    self.__queue.dequeue()
    self.assertEqual(len(self.__queue), 0)
  def test_2en2dequeuelen(self):
    self.__queue.enqueue(5)
    self.__queue.dequeue()
    self.__queue.enqueue(5)
    self.__queue.dequeue()
    self.assertEqual(len(self.__queue), 0)

  def test_endepeekqueuelen(self):
    self.__queue.enqueue(5)
    self.__queue.dequeue()
    self.__queue.peek()
    self.assertEqual(len(self.__queue), 0)
  def test_pendequeueval(self):
    self.__queue.enqueue(5)
    self.__queue.dequeue()
    x=self.__queue.peek()
    self.assertEqual(x, None)

  def test_endequeueopeekutput(self):
    self.__queue.enqueue(5)
    self.__queue.dequeue()
    self.__queue.peek()
    self.assertEqual('[ ]', str(self.__queue))

  def test_2en1dequeuepeeklen(self):
    self.__queue.enqueue(5)
    self.__queue.enqueue(5)
    self.__queue.dequeue()
    self.__queue.peek()
    self.assertEqual(len(self.__queue), 1)
  def test_2en1dequeupeekeval(self):
    self.__queue.enqueue(5)
    self.__queue.enqueue(5)
    self.__queue.dequeue()
    x=self.__queue.peek()
    self.assertEqual(x, 5)

  def test_2en1dequeuepeekoutput(self):
    self.__queue.enqueue(5)
    self.__queue.enqueue(5)
    self.__queue.dequeue()
    self.__queue.peek()
    self.assertEqual('[ 5 ]', str(self.__queue))
  def test_2enpeekqueueoutput(self):
    self.__queue.enqueue(5)
    self.__queue.enqueue(6)
    
    self.__queue.peek()
    self.assertEqual('[ 5, 6 ]', str(self.__queue))
  
  def test_2enpeekqueuelen(self):
    self.__queue.enqueue(6)
    self.__queue.enqueue(5)
    
    self.__queue.peek()
    self.assertEqual(2, len(self.__queue))
  
  def test_2endevalval(self):
    self.__queue.enqueue(6)
    self.__queue.enqueue(5)
    
    x=self.__queue.peek()
    self.assertEqual(6 , x)
  def test_3enqueueoutput(self):
    self.__queue.enqueue(3)
    self.__queue.enqueue(4)
    self.__queue.enqueue(5)
    self.assertEqual('[ 3, 4, 5 ]' , str(self.__queue))

  def test_3enqueuetacklength(self):
    self.__queue.enqueue(3)
    self.__queue.enqueue(4)
    self.__queue.enqueue(5)
    self.assertEqual( 3 , len(self.__queue))

  def test_3enqueueoutput1de(self):
    self.__queue.enqueue(3)
    self.__queue.enqueue(4)
    self.__queue.enqueue(5)
    self.__queue.dequeue()
    self.assertEqual('[ 4, 5 ]' , str(self.__queue))

  def test_3enqueuelength1de(self):
    self.__queue.enqueue(3)
    self.__queue.enqueue(4)
    self.__queue.enqueue(5)
    self.__queue.dequeue()
    self.assertEqual(2 , len(self.__queue))

  def test_3enqueueval1de(self):
    self.__queue.enqueue(3)
    self.__queue.enqueue(4)
    self.__queue.enqueue(5)
    x=self.__queue.dequeue()
    self.assertEqual( 3, x)

  def test_3enqueue1peek(self):
    self.__queue.enqueue(3)
    self.__queue.enqueue(4)
    self.__queue.enqueue(5)
    x=self.__queue.peek()
    self.assertEqual( 3, x)

  def test_3enqueueoutput2de(self):
    self.__queue.enqueue(3)
    self.__queue.enqueue(4)
    self.__queue.enqueue(5)
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.assertEqual('[ 5 ]' , str(self.__queue))

  def test_3enqueuelength2de(self):
    self.__queue.enqueue(3)
    self.__queue.enqueue(4)
    self.__queue.enqueue(5)
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.assertEqual(1 , len(self.__queue))

  def test_3enqueueval2de(self):
    self.__queue.enqueue(3)
    self.__queue.enqueue(4)
    self.__queue.enqueue(5)
    x=self.__queue.dequeue()
    x=self.__queue.dequeue()
    self.assertEqual(x, 4)

  def test_3enqueueoutput3de(self):
    self.__queue.enqueue(3)
    self.__queue.enqueue(4)
    self.__queue.enqueue(5)
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.assertEqual('[ ]' , str(self.__queue))

  def test_3enqueuelength3de(self):
    self.__queue.enqueue(3)
    self.__queue.enqueue(4)
    self.__queue.enqueue(5)
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.assertEqual(0 , len(self.__queue))

  def test_3enqueueval3de(self):
    self.__queue.enqueue(3)
    self.__queue.enqueue(4)
    self.__queue.enqueue(5)
    x=self.__queue.dequeue()
    x=self.__queue.dequeue()
    x=self.__queue.dequeue()
    self.assertEqual(x, 5)










  
  

if __name__ == '__main__':
  unittest.main()

