from multiprocessing.dummy import Value


class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class __BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class 
    # must be public to be reachable from the the methods.

    def __init__(self, value):
      self.value = value
      
      self.left=None
      self.right= None
      self.height=1
      
        

      
        
      # TODO complete Node initialization

  def __init__(self):
    self.__root = None

    
    # TODO complete initialization

  def insert_element(self, value):
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    # TODO replace pass with your implementation
    
    self.__root=self.__recursive_insert(value,self.__root)
    
    
    
    return self.__root
    
    


  def __recursive_insert(self,value,root):
    if root ==None:
      new_node= self.__BST_Node(value)
      return new_node
   
    else:
      
      if value > root.value:
        root.right=self.__recursive_insert(value,root.right)
        
          
        
        if root.height==root.right.height:
          root.height+=1
        
        return self.__balance(root)
        
      elif value < root.value:
       
        root.left=self.__recursive_insert(value,root.left)
        if root.height==root.left.height:
          root.height+=1
        
        
        return self.__balance(root)
      else:
        raise ValueError
    
  def __balance(self,t):
   
    if t ==None:
      return t       
    if t.right==None:
          r_height=0
    else:
      r_height=t.right.height
    if t.left==None:
      l_height=0
    else:
      l_height=t.left.height
    r_balance=r_height-l_height
    
    if r_balance ==2:
      rrr_height=0
      rrl_height=0
      if t.right.right!=None:
        rrr_height=t.right.right.height
      if t.right.left!=None:
        rrl_height=t.right.left.height

      rr_balance= rrr_height-rrl_height
      if rr_balance<0:
        t=self.__double_rotate(t,t.right,t.right.left)
      else:
        t=self.__rotate(t,t.right)
       
      return t
        
    elif r_balance ==-2:
      rlr_height=0
      rll_height=0
      if t.left.right!=None:
        rlr_height=t.left.right.height
      if t.left.left!=None:
        rll_height=t.left.left.height

      rl_balance= rlr_height-rll_height
      if rl_balance>0:
        t=self.__double_rotate(t,t.left,t.left.right)
      else:
        
        t=self.__rotate(t,t.left)

      return t
    else:
      
      return t


  def __rotate(self,node,child):
    
    temp_node=self.__BST_Node(child.value)
    
   
    if node.right!=None and child.value == node.right.value:


      temp_node.right=child.right
      temp_node.left=node
      
      temp_node.left.right=child.left
      if temp_node.left.right==None:
        temp_node.left.height =1
        temp_node.height=2
      else:
        temp_node.left.height= temp_node.left.right.height+1
        if temp_node.right!=None:
          if temp_node.left.height>temp_node.right.height:
            temp_node.height=temp_node.left.height+1
          else:
            temp_node.height=temp_node.right.height+1
        else:
          temp_node.height=temp_node.left.height+1
      
      
      return temp_node
    else:
      
      temp_node.left=child.left
      
      temp_node.right=node
      temp_node.right.left=child.right
     
      if temp_node.right.left==None and temp_node.right.right==None:
        temp_node.right.height =1
        temp_node.height=2
      elif temp_node.right.left==None:
        temp_node.height=temp_node.right.right.height+2
      elif temp_node.right.right==None:
        temp_node.height=temp_node.right.left.height+2
      
      else:
        
        temp_node.right.height= temp_node.right.left.height+1
        print(temp_node.value)
        if temp_node.left!=None:
          if temp_node.right.height>temp_node.left.height:
            temp_node.height=temp_node.right.height+1
          else:
            temp_node.height=temp_node.left.height+1
        else:
            temp_node.height=temp_node.right.height+1
      return temp_node


  def __double_rotate(self,node,child,inner_child):
    
    
    sub_tree=self.__rotate(child,inner_child)
    
    if child is node.right:
      node.right=sub_tree
    else:
      node.left=sub_tree
   
    new_tree=self.__rotate(node,sub_tree)
    
    return new_tree

  def remove_element(self, value):
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    # TODO replace pass with your implementation
    if self.__root==None:
      raise ValueError
    self.__root=self.__recursive_remove(value,self.__root)


  def __recursive_remove(self,value,node):
    if node.value==value:  
      if node.left ==None and node.right==None:
        node.height=0
        node=None   
        return node  
      elif node.right == None and node.left!=None:       
        node=node.left       
        return  self.__balance(node)

      elif node.left == None and node.right!=None:      
        node=node.right       
        return self.__balance(node)
      else:
      
        if node.value>self.__root.value:
          if node.right != None:   
            node.value=self.__replacement_value(node.right)     
            
          else:
            node.value=self.__replacement_value(node)
          if node.right !=None and node.left!=None:
            if node.right.height>node.left.height:
             node.height-=1 
        elif self.__root.value==node.value:
          node.value=self.__replacement_value(self.__root.right)
          node.right= node.right.right
          if node.right!=None:
            if node.right.right!=None:
              node.right=node.right.right
          
          if node.right !=None and node.left!=None:
            
            if node.right.height>node.left.height:
              node.height-=1  
                 
        else:
          
          node.value=self.__replacement_value(node.right)
          if node.right.height>node.left.height:
            node.height-=1      
          
    elif node.right ==None and node.left ==None:
      raise ValueError
    else: 
      if node.value > value:
        node.left=self.__recursive_remove(value,node.left) 
        if node.left != None and node.right!=None:
          if node.left.height >= node.right.height:
            node.height =node.left.height +1
          else:
            node.height =node.right.height +1
        elif node.left !=None:
          node.height =node.left.height +1
        elif node.right != None:
          node.height =node.right.height +1
        else:
          node.height=1     
      else:  
        node.right=self.__recursive_remove(value,node.right)
        if node.left != None and node.right!=None:
          if node.left.height >= node.right.height:
            node.height =node.left.height +1
          else:
            node.height =node.right.height +1
        elif node.left !=None:
          node.height =node.left.height +1
        elif node.right != None:
          node.height =node.right.height +1
        else:
          node.height=1  
    
    return self.__balance(node)
 
  def __replacement_value(self,node):
    
    current =node
    
    if node.left==None:
      if current.right!=None:
    
        node.right=current.right
     
      return node.value
    while current.left.left!=None:
      current=node.left
    
    x=current.left.value
    
    if current.left.right!=None:
      node.left=current.left.right
      return x
    current.left=None
    return x


      





      







  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    # TODO replace pass with your implementation
    if self.__root == None:
      return ('[ ]')  
    else: 
      return ('[ '+self.__recursive_walk_IO(self.__root)+' ]')
      

  def __recursive_walk_IO(self,node):
    if node.left != None or node.right != None:
      left_string=''
      right_string=''
      if node.left!= None:
        left_string=self.__recursive_walk_IO(node.left)
      root_string=str(node.value)
      if node.right!=None:
        right_string=self.__recursive_walk_IO(node.right)
      if left_string=='' and right_string=='':
        return root_string
      elif left_string=='':
        return root_string+', '+right_string
      elif right_string=='':
        return left_string+', '+root_string
      else:
        return left_string+', '+root_string+', '+right_string
      
      
    else:
      return str(node.value)
    
   
    









  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.__root == None:
      return ('[ ]')
    
    else: 
   
      return ('[ '+self.__recursive_walk_PRO(self.__root)+' ]')

  def __recursive_walk_PRO(self,node):
    if node.left != None or node.right != None:
      left_string=''
      right_string=''
      if node.left!= None:
        left_string=self.__recursive_walk_PRO(node.left)
      root_string=str(node.value)
      if node.right!=None:
        right_string=self.__recursive_walk_PRO(node.right)
      if left_string=='' and right_string=='':
        return root_string
      elif left_string=='':
        return root_string+', '+right_string
      elif right_string=='':
        return root_string+', '+left_string
      else:
        return root_string+', '+left_string+', '+right_string
      
      
    else:
      return str(node.value)

  def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.__root == None:
      return ('[ ]')
    
    else: 
   
      return ('[ '+self.__recursive_walk_PSO(self.__root)+' ]')

  def __recursive_walk_PSO(self,node):
    if node.left != None or node.right != None:
      left_string=''
      right_string=''
      root_string=''
      if node.left!= None:
        left_string=self.__recursive_walk_PSO(node.left)
        
      
      if node.right!=None:
        right_string=self.__recursive_walk_PSO(node.right)
        
      root_string=str(node.value)
      if left_string=='' and right_string=='':
        return root_string
      elif left_string=='':
        return right_string+', '+root_string
      elif right_string=='':
        return left_string+', '+root_string
      else:
        return left_string+', '+right_string+', '+root_string
      
      
    else:
      return str(node.value)


  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    # TODO replace pass with your implementation
    if self.__root ==None:
      return 0
    else:
      return self.__root.height 

  def __str__(self):
    
    return self.in_order()

if __name__ == '__main__':
  x = Binary_Search_Tree()
  
  x.insert_element(50)
  x.insert_element(30)
  x.insert_element(70)
  x.insert_element(60)
  x.insert_element(80)
  x.insert_element(65)
  
  
  
  

  

  
  
  print(x.get_height())
  print(x)
  print(x.pre_order())
  print(x.post_order())
  

