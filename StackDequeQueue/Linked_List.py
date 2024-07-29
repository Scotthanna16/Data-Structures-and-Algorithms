class Linked_List:
    
    class __Node:
        
        def __init__(self, val):
            # Declare and initialize the public attributes for objects of the
            # Node class. TODO replace pass with your implementation
            self.nodevalue=val
            self.next= None
            self.previous = None

    def __init__(self):
        # Declare and initialize the private attributes for objects of the
        # sentineled Linked_List class TODO replace pass with your
        # implementation
        self.__header= self.__Node(None)
        self.__trailer= self.__Node(None)
        self.__header.next=self.__trailer
        self.__trailer.previous=self.__header
        self.__size=0

    def __len__(self):
        # Return the number of value-containing nodes in this list. TODO replace
        # pass with your implementation
        return self.__size

    def append_element(self, val):
        # Increase the size of the list by one, and add a node containing val at
        # the new tail position. this is the only way to add items at the tail
        # position. TODO replace pass with your implementation

        # Do this next, only way to insert element when list size =0
        
        newest= self.__Node(val)
        newest.next=self.__trailer
        newest.previous=self.__trailer.previous
        self.__trailer.previous.next=newest
        self.__trailer.previous=newest
        self.__size+=1
       
    def insert_element_at(self, val, index):
        # Assuming the head position (not the header node) is indexed 0, add a
        # node containing val at the specified index. If the index is not a
        # valid position within the list, raise an IndexError exception. This
        # method cannot be used to add an item at the tail position. TODO
        # replace pass with your implementation

        # make a private current walk function that you can use in all element at methods

        if self.__size==0 or index>=self.__size:
            raise IndexError
       
        if index==0:
            current = self.__header
            newest=self.__Node(val)
            newest.next=current.next
            newest.previous = current
            current.next=newest
            newest.next.previous=newest
            self.__size+=1

        else:
            current = self.__current_walk(index)
            newest=self.__Node(val)
            newest.next=current.next
            newest.previous = current
            current.next=newest
            newest.next.previous=newest
            self.__size+=1

            
            


        
    def __current_walk(self, index):
        if index==0:
            return self.__header
        else:
            current=self.__header.next
            for _ in range(1,index):
                current=current.next
            return current


    def remove_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, remove
        # and return the value stored in the node at the specified index. If the
        # index is invalid, raise an IndexError exception. TODO replace pass
        # with your implementation
        if self.__size==0 or index>=self.__size:
            raise IndexError
        if index == self.__size-1:
            current=self.__trailer.previous.previous 
            value = self.__trailer.previous.nodevalue
            current.next.next.previous=current
            current.next=self.__trailer
            self.__size-=1
        elif self.__size == 1:
            current=self.__header
            value = current.next.nodevalue
            current.next.next.previous=current
            current.next=current.next.next
            self.__size-=1
        else:
            current=self.__current_walk(index)
            value = current.next.nodevalue
            current.next.next.previous=current
            current.next=current.next.next
            self.__size-=1
        return value


    def get_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, return
        # the value stored in the node at the specified index, but do not unlink
        # it from the list. If the specified index is invalid, raise an
        # IndexError exception. TODO replace pass with your implementation
        if self.__size==0 or index>=self.__size:
            raise IndexError
        elif index == self.__size-1:
            current=self.__trailer.previous
            return current.nodevalue
        elif self.__size == 1:
            current=self.__header.next
            return current.nodevalue
        else: 
            current=self.__current_walk(index+1)
            return current.nodevalue


    def rotate_left(self):
        # Rotate the list left one position. Conceptual indices should all
        # decrease by one, except for the head, which should become the tail.
        # For example, if the list is [ 5, 7, 9, -4 ], this method should alter
        # it to [ 7, 9, -4, 5 ]. This method should modify the list in place and
        # must not return a value. TODO replace pass with your implementation.

        # this has to be done by relinking the the head after the tail and the the header to what was head.next to make it constant time
        if self.__size==0:
            return
        else:
            
            value = self.__header.next.nodevalue
            current=self.__header.next
            for _ in range(1,self.__size,1):
                current.nodevalue= current.next.nodevalue
                current=current.next
            self.__trailer.previous.nodevalue=value

        
    def __str__(self):
        # Return a string representation of the list's contents. An empty list
        # should appear as [ ]. A list with one element should appear as [ 5 ].
        # A list with two elements should appear as [ 5, 7 ]. You may assume
        # that the values stored inside of the node objects implement the
        # __str__() method, so you call str(val_object) on them to get their
        # string representations. TODO replace pass with your implementation


        # do this after append, doesnt have to be perfect, but make it functional and come back later 
        if self.__size==0:
            return '[ ]'
        elif self.__size==1:
            return ('[ '+str(self.__header.next.nodevalue)+' ]')
        else:
            current=self.__header.next
            string= str(current.nodevalue) + ', '
            current=current.next
            while current is not self.__trailer.previous:
                string = string + str(current.nodevalue) + ', '
                current=current.next
        return ('[ '+string+ str(self.__trailer.previous.nodevalue)+' ]')

    def __iter__(self):
        # Initialize a new attribute for walking through your list TODO insert
        # your initialization code before the return statement. Do not modify
        # the return statement.
       
        self.__iter_index = self.__header.next
        return self

    def __next__(self):
        # Using the attribute that you initialized in __iter__(), fetch the next
        # value and return it. If there are no more values to fetch, raise a
        # StopIteration exception. TODO replace pass with your implementation
        
        if self.__iter_index is self.__trailer:
            raise StopIteration
    # each time a new value is requested (such as
    # a cycle in a for loop), grab the value, up the
    # index to prepare for the next call, and return
    # the value.
        to_return = self.__iter_index.nodevalue
        self.__iter_index = self.__iter_index.next
        return to_return

    def __reversed__(self):
        # Construct and return a new Linked_List object whose nodes alias t
        # same objects as the nodes in this list, but in reverse order. For a
        # Linked_List object ll, Python will automatically call this function
        # when it encounters a call to reversed(ll) in an application. If
        # print(ll) displays [ 1, 2, 3, 4, 5 ], then print(reversed(ll)) should
        # display [ 5, 4, 3, 2, 1 ]. This method does not change the state of
        # the object on which it is called. Calling print(ll) again will still
        # display [ 1, 2, 3, 4, 5 ], even after calling reversed(ll). This
        # method must operate in linear time.
        if self.__size==0:
            return self
        else:
            y=Linked_List()
            value = self.__trailer.previous.nodevalue
            current = self.__trailer.previous
            list=[value]
            current=current.previous
            for _ in range(self.__size,1,-1):
                q=current.nodevalue
                list.append(q)
                current=current.previous
            
    
            y.append_element(list[0])

            for x in range(1,self.__size,1):
                y.append_element(list[x])

            return y





            

if __name__ == '__main__':
    x = Linked_List()
    print(x)
    x.append_element(4)
    print(x)
    x.append_element(2)
    print(x)
    x.insert_element_at(1,0)
    print(x)
    x.remove_element_at(0)
    print(x)
    x.remove_element_at(1)
    print(x)
    x.append_element(6)
    x.insert_element_at(2,1)
    x.append_element(3)
    x.insert_element_at(5,2)
    print(x)
    print(x.remove_element_at(1))
    print(x)
    print(x.remove_element_at(3))
    print(x)
    print(x.get_element_at(1))
    print(x)
    x.rotate_left()
    print(x)
    print(reversed(x))
    x.insert_element_at(2,1)
    x.append_element(3)
    x.insert_element_at(5,2)
    print(x)
    print(reversed(x))
    print(x)
    for val in x:
        print(val)
    y = Linked_List()
    y.append_element(3)
    print(y)
    print(reversed(y))
    y.insert_element_at(4,0)
    y.insert_element_at(5,1)
    print(y)
    print(reversed(y))
    y.remove_element_at(2)
    print(y)
    z= Linked_List()
    try:
        z.insert_element_at(5,0)
    except IndexError:
        print("Correct, error expected")
    z.append_element(3)
    z.append_element(4)
    z.append_element(5)
    try:
        z.insert_element_at(2,3)
    except IndexError:
        print("Correct, error expected")
    q = Linked_List()
    try:
        q.remove_element_at(0)
    except IndexError:
        print("Correct, error expected")
    q.append_element(2)
    try:
        q.remove_element_at(1)
    except IndexError:
        print("Correct, error expected")
    for val in reversed(x):
        print(val)
    print(len(x))
    #x.remove_element_at(7)
    print(x)

    t=Linked_List()
    print(t)
    print(reversed(t))




    



  