
def test_empty_tree_tolst(self):
    x=self.__BST
    self.assertEqual(x.to_list(), [])
def test_empty_tree_tolist(self):
    x=self.__BST
    
    self.assertEqual(x.to_list(), [])
    
def test_oneinsert_tree_tolist(self):
    x=self.__BST
    x.insert_element(3)

    self.assertEqual(x.to_list(), [3])
    

def test_twoinsert_tree_tolist(self):
    x=self.__BST
    x.insert_element(3)
    x.insert_element(5)

    self.assertEqual(x.to_list(), [3, 5])
    
def test_threeinsert_tree_tolist(self):
    x=self.__BST
    x.insert_element(3)
    x.insert_element(5)
    x.insert_element(1)
    
    self.assertEqual(x.to_list(), [1, 3, 5])
    

def test_threeinsert_treerotationleft_tolist(self):
    x=self.__BST
    x.insert_element(3)
    x.insert_element(5)
    x.insert_element(7)
    
    self.assertEqual(x.to_list(), [3, 5, 7])


def test_threeinsert_treerotationright_tolist(self):
    x=self.__BST
    x.insert_element(7)
    x.insert_element(5)
    x.insert_element(3)
    
    self.assertEqual(x.to_list(), [3, 5, 7])
    


def test_fiveinsert_treerotationright_tolist(self):
    x=self.__BST
    x.insert_element(7)
    x.insert_element(5)
    x.insert_element(9)
    x.insert_element(3)
    x.insert_element(2)

    self.assertEqual(x.to_list(), [2, 3, 5, 7, 9])



def test_fiveinsert_treerotationleft_tolist(self):
    x=self.__BST
    x.insert_element(7)
    x.insert_element(5)
    x.insert_element(9)
    x.insert_element(11)
    x.insert_element(13)

    self.assertEqual(x.to_list(), [5, 7, 9, 11, 13])


def test_three_insert_doublerotationrightleft_list(self):
    x=self.__BST
    x.insert_element(7)
    x.insert_element(11)
    x.insert_element(9)

    self.assertEqual(x.to_list(), [7, 9, 11])
    


def test_three_insert_doublerotationleftright_list(self):
    x=self.__BST
    x.insert_element(7)
    x.insert_element(5)
    x.insert_element(6)

    self.assertEqual(x.to_list(), [5, 6, 7])





def test_five_insert_doublerotationleftright_list(self):
    x=self.__BST
    x.insert_element(7)
    x.insert_element(8)
    x.insert_element(6)
    x.insert_element(4)
    x.insert_element(5)

    self.assertEqual(x.to_list(), [4, 5, 6, 7, 8])
    


def test_five_insert_doublerotationleftrightleft_list(self):
    x=self.__BST
    x.insert_element(7)
    x.insert_element(8)
    x.insert_element(6)
    x.insert_element(10)
    x.insert_element(9)
    
    self.assertEqual(x.to_list(), [6, 7, 8, 9, 10])
    



def test_6float_insert_doublerotationrightleft1_list(self):
    x=self.__BST
    x.insert_element(7)
    x.insert_element(8)
    x.insert_element(6)
    x.insert_element(10)
    x.insert_element(9)
    x.insert_element(11)

    self.assertEqual(x.to_list(), [6, 7, 8, 9, 10, 11])



def test_6float_insert_doublerotationrightleft2_list(self):
    x=self.__BST
    x.insert_element(7)
    x.insert_element(10)
    x.insert_element(6)
    x.insert_element(9)
    x.insert_element(12)
    x.insert_element(11)
    
    self.assertEqual(x.to_list(), [6, 7, 9, 10, 11, 12])
    


def test_6float_insert_no_rot_list(self):
    x=self.__BST
    x.insert_element(7)
    x.insert_element(11)
    x.insert_element(6)
    x.insert_element(8)
    x.insert_element(12)
    x.insert_element(9)

    self.assertEqual(x.to_list(), [6, 7, 8, 9, 11, 12])
    



def test_6float_insert_no_rot2_list(self):
    x=self.__BST
    x.insert_element(7)
    x.insert_element(11)
    x.insert_element(6)
    x.insert_element(9)
    x.insert_element(12)
    x.insert_element(8)

    self.assertEqual(x.to_list(), [6, 7, 8, 9, 11, 12])





def test_6float_insert_rotationright_list(self):
    x=self.__BST
    x.insert_element(7)
    x.insert_element(8)
    x.insert_element(5)
    x.insert_element(6)
    x.insert_element(4)
    x.insert_element(3)
    
    self.assertEqual(x.to_list(), [3, 4, 5, 6, 7, 8])
    




def test_insertthenremovelist(self):
    x=self.__BST
    x.insert_element(8)
    x.remove_element(8)

    self.assertEqual(x.to_list(), [])
    


    

def test_insert2thenremovelist(self):
    x=self.__BST
    x.insert_element(8)
    x.insert_element(9)
    x.remove_element(9)

    self.assertEqual(x.to_list(), [8])



    

def test_insert2thenremoverootlist(self):
    x=self.__BST
    x.insert_element(8)
    x.insert_element(9)
    x.remove_element(8)
    
    self.assertEqual(x.to_list(), [9])
    



    

def test_insert3thenremoverightlist(self):
    x=self.__BST
    x.insert_element(8)
    x.insert_element(7)
    x.insert_element(9)
    x.remove_element(9)
    
    self.assertEqual(x.to_list(), [7, 8])
    


    

def test_insert3thenremoveleftlist(self):
    x=self.__BST
    x.insert_element(8)
    x.insert_element(7)
    x.insert_element(9)
    x.remove_element(7)

    self.assertEqual(x.to_list(), [8, 9])




def test_insert3thenremoverootlist(self):
    x=self.__BST
    x.insert_element(8)
    x.insert_element(7)
    x.insert_element(9)
    x.remove_element(8)
    
    self.assertEqual(x.to_list(), [7, 9])





def test_insert3rotateleftremoveleftlist(self):
    x=self.__BST
    x.insert_element(8)
    x.insert_element(9)
    x.insert_element(10)
    x.remove_element(8)

    self.assertEqual(x.to_list(), [9, 10])
    



def test_insert3rotateleftremoverighlist(self):
    x=self.__BST
    x.insert_element(8)
    x.insert_element(9)
    x.insert_element(10)
    x.remove_element(10)
    
    self.assertEqual(x.to_list(), [8, 9])
    



def test_insert3rotateleftremoveroolist(self):
    x=self.__BST
    x.insert_element(8)
    x.insert_element(9)
    x.insert_element(10)
    x.remove_element(9)
    
    self.assertEqual(x.to_list(), [8, 10])
    



def test_insert3doublerotateleftremoveeleftlist(self):
    x=self.__BST
    x.insert_element(8)
    x.insert_element(10)
    x.insert_element(9)
    x.remove_element(8)
    
    self.assertEqual(x.to_list(), [9, 10])
    


def test_insert3doublerotateleftremoveerootlist(self):
    x=self.__BST
    x.insert_element(8)
    x.insert_element(10)
    x.insert_element(9)
    x.remove_element(9)
    
    self.assertEqual(x.to_list(), [8, 10])
    



def test_insert3doublerotateleftremoveerightlist(self):
    x=self.__BST
    x.insert_element(8)
    x.insert_element(10)
    x.insert_element(9)
    x.remove_element(10)

    self.assertEqual(x.to_list(), [8, 9])




def test_insert3rotaterightremoveleftlist(self):
    x=self.__BST
    x.insert_element(8)
    x.insert_element(7)
    x.insert_element(6)
    x.remove_element(6)
    
    self.assertEqual(x.to_list(), [7, 8])


def test_insert3rotaterightremoverighlist(self):
    x=self.__BST
    x.insert_element(8)
    x.insert_element(7)
    x.insert_element(6)
    x.remove_element(8)
    
    self.assertEqual(x.to_list(), [6, 7])
    


def test_insert3rotaterightremoveroolist(self):
    x=self.__BST
    x.insert_element(8)
    x.insert_element(7)
    x.insert_element(6)
    x.remove_element(7)
    
    self.assertEqual(x.to_list(), [6, 8])
    


def test_insert3doublerotaterightremoveeleftlist(self):
    x=self.__BST
    x.insert_element(8)
    x.insert_element(6)
    x.insert_element(7)
    x.remove_element(6)
    
    self.assertEqual(x.to_list(), [7, 8])
    



def test_insert3doublerotaterightremoveerightlist(self):
    x=self.__BST
    x.insert_element(8)
    x.insert_element(6)
    x.insert_element(7)
    x.remove_element(8)
    
    self.assertEqual(x.to_list(), [6, 7])




def test_insert3doublerotaterightremoveerootlist(self):
    x=self.__BST
    x.insert_element(8)
    x.insert_element(6)
    x.insert_element(7)
    x.remove_element(7)
    
    self.assertEqual(x.to_list(), [6, 8])
    


















def test_inserting4andremovingrootrotatelist(self):
    x=self.__BST
    x.insert_element(8)
    x.insert_element(6)
    x.insert_element(9)
    x.insert_element(5)
    x.remove_element(8)

    self.assertEqual(x.to_list(), [5, 6, 9])





def test_inserting5andremovingrootrotatelist(self):
    x=self.__BST
    x.insert_element(8)
    x.insert_element(6)
    x.insert_element(9)
    x.insert_element(10)
    x.insert_element(5)
    x.remove_element(8)
    
    self.assertEqual(x.to_list(), [5, 6, 9, 10])
    




def test_inserting6andremovingrootrotatelist(self):
    x=self.__BST
    x.insert_element(8)
    x.insert_element(6)
    x.insert_element(10)
    x.insert_element(11)
    x.insert_element(9)
    x.insert_element(5)
    x.remove_element(8)
    
    self.assertEqual(x.to_list(), [5, 6, 9, 10, 11])