import unittest
from Binary_Search_Tree import Binary_Search_Tree
from Fraction import Fraction


class BST_Test(unittest.TestCase):
    def setUp(self):
        self.__fraction = Fraction(numerator=1, denominator=1)
        self.__BST = Binary_Search_Tree()

    def test_empty_tree_height(self):
        x=self.__BST
        self.assertEqual(x.get_height(), 0)
    def test_empty_tree_inorder(self):
        x=self.__BST
        self.assertEqual(x.in_order(), '[ ]')
    def test_empty_tree_inorderprepost(self):
        x=self.__BST
        self.assertEqual(x.pre_order(), '[ ]')
        self.assertEqual(x.in_order(), '[ ]')
        self.assertEqual(x.post_order(), '[ ]')
    def test_one_insertion_height(self):
        x=self.__BST
        x.insert_element(3)
        self.assertEqual(x.get_height(), 1)
    def test_oneinsert_tree_inorderprepost(self):
        x=self.__BST
        x.insert_element(3)
        self.assertEqual(x.pre_order(), '[ 3 ]')
        self.assertEqual(x.in_order(), '[ 3 ]')
        self.assertEqual(x.post_order(), '[ 3 ]')
    def test_two_insertion_height(self):
        x=self.__BST
        x.insert_element(3)
        x.insert_element(5)
        self.assertEqual(x.get_height(), 2)
    def test_twoinsert_tree_inorderprepost(self):
        x=self.__BST
        x.insert_element(3)
        x.insert_element(5)
        self.assertEqual(x.pre_order(), '[ 3, 5 ]')
        self.assertEqual(x.in_order(), '[ 3, 5 ]')
        self.assertEqual(x.post_order(), '[ 5, 3 ]')
    def test_three_insertion_height(self):
        x=self.__BST
        x.insert_element(3)
        x.insert_element(5)
        x.insert_element(1)
        self.assertEqual(x.get_height(), 2)
    def test_threeinsert_tree_inorderprepost(self):
        x=self.__BST
        x.insert_element(3)
        x.insert_element(5)
        x.insert_element(1)
        self.assertEqual(x.pre_order(), '[ 3, 1, 5 ]')
        self.assertEqual(x.in_order(), '[ 1, 3, 5 ]')
        self.assertEqual(x.post_order(), '[ 1, 5, 3 ]')
    def test_three_insertionrotationleft_height(self):
        x=self.__BST
        x.insert_element(3)
        x.insert_element(5)
        x.insert_element(7)
        self.assertEqual(x.get_height(), 2)
    def test_threeinsert_treerotationleft_inorderprepost(self):
        x=self.__BST
        x.insert_element(3)
        x.insert_element(5)
        x.insert_element(7)
        self.assertEqual(x.pre_order(), '[ 5, 3, 7 ]')
        self.assertEqual(x.in_order(), '[ 3, 5, 7 ]')
        self.assertEqual(x.post_order(), '[ 3, 7, 5 ]')
    def test_three_insertionrotationright_height(self):
        x=self.__BST
        x.insert_element(7)
        x.insert_element(5)
        x.insert_element(3)
        self.assertEqual(x.get_height(), 2)
    def test_threeinsert_treerotationright_inorderprepost(self):
        x=self.__BST
        x.insert_element(7)
        x.insert_element(5)
        x.insert_element(3)
        self.assertEqual(x.pre_order(), '[ 5, 3, 7 ]')
        self.assertEqual(x.in_order(), '[ 3, 5, 7 ]')
        self.assertEqual(x.post_order(), '[ 3, 7, 5 ]')

    def test_five_insertionrotationright_height(self):
        x=self.__BST
        x.insert_element(7)
        x.insert_element(5)
        x.insert_element(9)
        x.insert_element(3)
        x.insert_element(2)
        self.assertEqual(x.get_height(), 3)
    def test_fiveinsert_treerotationright_inorderprepost(self):
        x=self.__BST
        x.insert_element(7)
        x.insert_element(5)
        x.insert_element(9)
        x.insert_element(3)
        x.insert_element(2)
        self.assertEqual(x.pre_order(), '[ 7, 3, 2, 5, 9 ]')
        self.assertEqual(x.in_order(), '[ 2, 3, 5, 7, 9 ]')
        self.assertEqual(x.post_order(), '[ 2, 5, 3, 9, 7 ]')
    

    def test_five_insertionrotationleft_height(self):
        x=self.__BST
        x.insert_element(7)
        x.insert_element(5)
        x.insert_element(9)
        x.insert_element(11)
        x.insert_element(13)
        self.assertEqual(x.get_height(), 3)
    def test_fiveinsert_treerotationleft_inorderprepost(self):
        x=self.__BST
        x.insert_element(7)
        x.insert_element(5)
        x.insert_element(9)
        x.insert_element(11)
        x.insert_element(13)
        self.assertEqual(x.pre_order(), '[ 7, 5, 11, 9, 13 ]')
        self.assertEqual(x.in_order(), '[ 5, 7, 9, 11, 13 ]')
        self.assertEqual(x.post_order(), '[ 5, 9, 13, 11, 7 ]')

    def test_three_insert_doublerotationrightleft_height(self):
        x=self.__BST
        x.insert_element(7)
        x.insert_element(11)
        x.insert_element(9)
        self.assertEqual(x.get_height(), 2)
    def test_three_insert_doublerotationrightleft_traversals(self):
        x=self.__BST
        x.insert_element(7)
        x.insert_element(11)
        x.insert_element(9)
        self.assertEqual(x.pre_order(), '[ 9, 7, 11 ]')
        self.assertEqual(x.in_order(), '[ 7, 9, 11 ]')
        self.assertEqual(x.post_order(), '[ 7, 11, 9 ]')
    
    def test_three_insert_doublerotationleftright_height(self):
        x=self.__BST
        x.insert_element(7)
        x.insert_element(5)
        x.insert_element(6)
        self.assertEqual(x.get_height(), 2)
    def test_three_insert_doublerotationleftright_traversals(self):
        x=self.__BST
        x.insert_element(7)
        x.insert_element(5)
        x.insert_element(6)
        self.assertEqual(x.pre_order(), '[ 6, 5, 7 ]')
        self.assertEqual(x.in_order(), '[ 5, 6, 7 ]')
        self.assertEqual(x.post_order(), '[ 5, 7, 6 ]')

    
    def test_five_insert_doublerotationleftright_height(self):
        x=self.__BST
        x.insert_element(7)
        x.insert_element(8)
        x.insert_element(6)
        x.insert_element(4)
        x.insert_element(5)
        self.assertEqual(x.get_height(), 3)


    def test_five_insert_doublerotationleftright_traversals(self):
        x=self.__BST
        x.insert_element(7)
        x.insert_element(8)
        x.insert_element(6)
        x.insert_element(4)
        x.insert_element(5)
        self.assertEqual(x.pre_order(), '[ 7, 5, 4, 6, 8 ]')
        self.assertEqual(x.in_order(), '[ 4, 5, 6, 7, 8 ]')
        self.assertEqual(x.post_order(), '[ 4, 6, 5, 8, 7 ]')

    def test_five_insert_doublerotationrighteft_height(self):
        x=self.__BST
        x.insert_element(7)
        x.insert_element(8)
        x.insert_element(6)
        x.insert_element(10)
        x.insert_element(9)
        self.assertEqual(x.get_height(), 3)
    def test_five_insert_doublerotationleftrightleft_traversals(self):
        x=self.__BST
        x.insert_element(7)
        x.insert_element(8)
        x.insert_element(6)
        x.insert_element(10)
        x.insert_element(9)
        self.assertEqual(x.pre_order(), '[ 7, 6, 9, 8, 10 ]')
        self.assertEqual(x.in_order(), '[ 6, 7, 8, 9, 10 ]')
        self.assertEqual(x.post_order(), '[ 6, 8, 10, 9, 7 ]')
    

    def test_6float_insert_rotationerightleft1_height(self):
        x=self.__BST
        x.insert_element(7)
        x.insert_element(8)
        x.insert_element(6)
        x.insert_element(10)
        x.insert_element(9)
        x.insert_element(11)
        self.assertEqual(x.get_height(), 3)

    def test_6float_insert_doublerotationrightleft1_traversals(self):
        x=self.__BST
        x.insert_element(7)
        x.insert_element(8)
        x.insert_element(6)
        x.insert_element(10)
        x.insert_element(9)
        x.insert_element(11)
        self.assertEqual(x.pre_order(), '[ 9, 7, 6, 8, 10, 11 ]')
        self.assertEqual(x.in_order(), '[ 6, 7, 8, 9, 10, 11 ]')
        self.assertEqual(x.post_order(), '[ 6, 8, 7, 11, 10, 9 ]')

    def test_6float_insert_rotationerigtleft2_height(self):
        x=self.__BST
        x.insert_element(7)
        x.insert_element(10)
        x.insert_element(6)
        x.insert_element(9)
        x.insert_element(12)
        x.insert_element(11)
        self.assertEqual(x.get_height(), 3)

    def test_6float_insert_doublerotationrightleft2_traversals(self):
        x=self.__BST
        x.insert_element(7)
        x.insert_element(10)
        x.insert_element(6)
        x.insert_element(9)
        x.insert_element(12)
        x.insert_element(11)
        self.assertEqual(x.pre_order(), '[ 10, 7, 6, 9, 12, 11 ]')
        self.assertEqual(x.in_order(), '[ 6, 7, 9, 10, 11, 12 ]')
        self.assertEqual(x.post_order(), '[ 6, 9, 7, 11, 12, 10 ]')

    def test_6float_insert_no_rot_height(self):
        x=self.__BST
        x.insert_element(7)
        x.insert_element(11)
        x.insert_element(6)
        x.insert_element(8)
        x.insert_element(12)
        x.insert_element(9)
        self.assertEqual(x.get_height(), 3)

    def test_6float_insert_no_rot_traversals(self):
        x=self.__BST
        x.insert_element(7)
        x.insert_element(11)
        x.insert_element(6)
        x.insert_element(8)
        x.insert_element(12)
        x.insert_element(9)
        self.assertEqual(x.pre_order(), '[ 8, 7, 6, 11, 9, 12 ]')
        self.assertEqual(x.in_order(), '[ 6, 7, 8, 9, 11, 12 ]')
        self.assertEqual(x.post_order(), '[ 6, 7, 9, 12, 11, 8 ]')
    
    def test_6float_insert_no_rot2_height(self):
        x=self.__BST
        x.insert_element(7)
        x.insert_element(11)
        x.insert_element(6)
        x.insert_element(9)
        x.insert_element(12)
        x.insert_element(8)
        self.assertEqual(x.get_height(), 3)

    def test_6float_insert_no_rot2_traversals(self):
        x=self.__BST
        x.insert_element(7)
        x.insert_element(11)
        x.insert_element(6)
        x.insert_element(9)
        x.insert_element(12)
        x.insert_element(8)
        self.assertEqual(x.pre_order(), '[ 9, 7, 6, 8, 11, 12 ]')
        self.assertEqual(x.in_order(), '[ 6, 7, 8, 9, 11, 12 ]')
        self.assertEqual(x.post_order(), '[ 6, 8, 7, 12, 11, 9 ]')


    def test_6float_insert_rotationeright_height(self):
        x=self.__BST
        x.insert_element(7)
        x.insert_element(8)
        x.insert_element(5)
        x.insert_element(6)
        x.insert_element(4)
        x.insert_element(3)
        self.assertEqual(x.get_height(), 3)

    def test_6float_insert_rotationright_traversals(self):
        x=self.__BST
        x.insert_element(7)
        x.insert_element(8)
        x.insert_element(5)
        x.insert_element(6)
        x.insert_element(4)
        x.insert_element(3)
        self.assertEqual(x.pre_order(), '[ 5, 4, 3, 7, 6, 8 ]')
        self.assertEqual(x.in_order(), '[ 3, 4, 5, 6, 7, 8 ]')
        self.assertEqual(x.post_order(), '[ 3, 4, 6, 8, 7, 5 ]')
    
    def test_remove_from_emtpy_list(self):
        x=self.__BST
        
        with self.assertRaises(ValueError):
            x.remove_element(50)


    def test_insert_duplicate_root(self):
        x=self.__BST
        x.insert_element(7)
        with self.assertRaises(ValueError):
            x.insert_element(7)

    def test_insert_duplicate_value(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(7)

        with self.assertRaises(ValueError):
            x.insert_element(7)
    
    def test_insertthenremovehieght(self):
        x=self.__BST
        x.insert_element(8)
        x.remove_element(8)
        self.assertEqual(x.get_height(), 0)
        

    def test_insertthenremovetraversals(self):
        x=self.__BST
        x.insert_element(8)
        x.remove_element(8)
        self.assertEqual(x.pre_order(), '[ ]')
        self.assertEqual(x.in_order(), '[ ]')
        self.assertEqual(x.post_order(), '[ ]')

    def test_insert2thenremovevaluehieght(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(9)
        x.remove_element(9)
        self.assertEqual(x.get_height(), 1)
        

    def test_insert2thenremovetraversals(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(9)
        x.remove_element(9)
        self.assertEqual(x.pre_order(), '[ 8 ]')
        self.assertEqual(x.in_order(), '[ 8 ]')
        self.assertEqual(x.post_order(), '[ 8 ]')
    
    def test_insert2thenremoveroothieght(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(9)
        x.remove_element(8)
        self.assertEqual(x.get_height(), 1)
        

    def test_insert2thenremoveroottraversals(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(9)
        x.remove_element(8)
        self.assertEqual(x.pre_order(), '[ 9 ]')
        self.assertEqual(x.in_order(), '[ 9 ]')
        self.assertEqual(x.post_order(), '[ 9 ]')

    
    def test_insert3thenremoverighthieght(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(7)
        x.insert_element(9)
        x.remove_element(9)
        self.assertEqual(x.get_height(), 2)
        

    def test_insert3thenremoverighttraversals(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(7)
        x.insert_element(9)
        x.remove_element(9)
        self.assertEqual(x.pre_order(), '[ 8, 7 ]')
        self.assertEqual(x.in_order(), '[ 7, 8 ]')
        self.assertEqual(x.post_order(), '[ 7, 8 ]')

    def test_insert3thenremovelefthieght(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(7)
        x.insert_element(9)
        x.remove_element(7)
        self.assertEqual(x.get_height(), 2)
        

    def test_insert3thenremovelefttraversals(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(7)
        x.insert_element(9)
        x.remove_element(7)
        self.assertEqual(x.pre_order(), '[ 8, 9 ]')
        self.assertEqual(x.in_order(), '[ 8, 9 ]')
        self.assertEqual(x.post_order(), '[ 9, 8 ]')

    def test_insert3thenremoveroothieght(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(7)
        x.insert_element(9)
        x.remove_element(8)
        self.assertEqual(x.get_height(), 2)
    
    def test_insert3thenremoveroottraversals(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(7)
        x.insert_element(9)
        x.remove_element(8)
        self.assertEqual(x.pre_order(), '[ 9, 7 ]')
        self.assertEqual(x.in_order(), '[ 7, 9 ]')
        self.assertEqual(x.post_order(), '[ 7, 9 ]')
    

    def test_insert3rotateleftremoveleftheight(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(9)
        x.insert_element(10)
        x.remove_element(8)
        self.assertEqual(x.get_height(), 2)

    def test_insert3rotateleftremovelefttraversals(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(9)
        x.insert_element(10)
        x.remove_element(8)
        self.assertEqual(x.pre_order(), '[ 9, 10 ]')
        self.assertEqual(x.in_order(), '[ 9, 10 ]')
        self.assertEqual(x.post_order(), '[ 10, 9 ]')

    def test_insert3rotateleftremoverightheight(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(9)
        x.insert_element(10)
        x.remove_element(10)
        self.assertEqual(x.get_height(), 2)

    def test_insert3rotateleftremoverightraversals(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(9)
        x.insert_element(10)
        x.remove_element(10)
        self.assertEqual(x.pre_order(), '[ 9, 8 ]')
        self.assertEqual(x.in_order(), '[ 8, 9 ]')
        self.assertEqual(x.post_order(), '[ 8, 9 ]')

    def test_insert3rotateleftremoverootheight(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(9)
        x.insert_element(10)
        x.remove_element(9)
        self.assertEqual(x.get_height(), 2)

    def test_insert3rotateleftremoverootraversals(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(9)
        x.insert_element(10)
        x.remove_element(9)
        self.assertEqual(x.pre_order(), '[ 10, 8 ]')
        self.assertEqual(x.in_order(), '[ 8, 10 ]')
        self.assertEqual(x.post_order(), '[ 8, 10 ]')

    def test_insert3doublerotateleftremoveleftheight(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(10)
        x.insert_element(9)
        x.remove_element(8)
        self.assertEqual(x.get_height(), 2)

    def test_insert3doublerotateleftremoveelefttraversals(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(10)
        x.insert_element(9)
        x.remove_element(8)
        self.assertEqual(x.pre_order(), '[ 9, 10 ]')
        self.assertEqual(x.in_order(), '[ 9, 10 ]')
        self.assertEqual(x.post_order(), '[ 10, 9 ]')

    def test_insert3doublerotateleftremoverootheight(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(10)
        x.insert_element(9)
        x.remove_element(9)
        self.assertEqual(x.get_height(), 2)

    def test_insert3doublerotateleftremoveeroottraversals(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(10)
        x.insert_element(9)
        x.remove_element(9)
        self.assertEqual(x.pre_order(), '[ 10, 8 ]')
        self.assertEqual(x.in_order(), '[ 8, 10 ]')
        self.assertEqual(x.post_order(), '[ 8, 10 ]')

    def test_insert3doublerotateleftremoverightheight(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(10)
        x.insert_element(9)
        x.remove_element(10)
        self.assertEqual(x.get_height(), 2)

    def test_insert3doublerotateleftremoveerighttraversals(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(10)
        x.insert_element(9)
        x.remove_element(10)
        self.assertEqual(x.pre_order(), '[ 9, 8 ]')
        self.assertEqual(x.in_order(), '[ 8, 9 ]')
        self.assertEqual(x.post_order(), '[ 8, 9 ]')


























    def test_insert3rotaterightremoveleftheight(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(7)
        x.insert_element(6)
        x.remove_element(6)
        self.assertEqual(x.get_height(), 2)

    def test_insert3rotaterightremovelefttraversals(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(7)
        x.insert_element(6)
        x.remove_element(6)
        self.assertEqual(x.pre_order(), '[ 7, 8 ]')
        self.assertEqual(x.in_order(), '[ 7, 8 ]')
        self.assertEqual(x.post_order(), '[ 8, 7 ]')

    def test_insert3rotaterightremoverightheight(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(7)
        x.insert_element(6)
        x.remove_element(8)
        self.assertEqual(x.get_height(), 2)

    def test_insert3rotaterightremoverightraversals(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(7)
        x.insert_element(6)
        x.remove_element(8)
        self.assertEqual(x.pre_order(), '[ 7, 6 ]')
        self.assertEqual(x.in_order(), '[ 6, 7 ]')
        self.assertEqual(x.post_order(), '[ 6, 7 ]')

    def test_insert3rotaterightremoverootheight(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(7)
        x.insert_element(6)
        x.remove_element(7)
        self.assertEqual(x.get_height(), 2)

    def test_insert3rotaterightremoverootraversals(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(7)
        x.insert_element(6)
        x.remove_element(7)
        self.assertEqual(x.pre_order(), '[ 8, 6 ]')
        self.assertEqual(x.in_order(), '[ 6, 8 ]')
        self.assertEqual(x.post_order(), '[ 6, 8 ]')

    def test_insert3doublerotaterighttremoveleftheight(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(6)
        x.insert_element(7)
        x.remove_element(6)
        self.assertEqual(x.get_height(), 2)

    def test_insert3doublerotaterightremoveelefttraversals(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(6)
        x.insert_element(7)
        x.remove_element(6)
        self.assertEqual(x.pre_order(), '[ 7, 8 ]')
        self.assertEqual(x.in_order(), '[ 7, 8 ]')
        self.assertEqual(x.post_order(), '[ 8, 7 ]')

    def test_insert3doublerotaterightremoverightheight(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(6)
        x.insert_element(7)
        x.remove_element(8)
        self.assertEqual(x.get_height(), 2)

    def test_insert3doublerotaterightremoveerighttraversals(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(6)
        x.insert_element(7)
        x.remove_element(8)
        self.assertEqual(x.pre_order(), '[ 7, 6 ]')
        self.assertEqual(x.in_order(), '[ 6, 7 ]')
        self.assertEqual(x.post_order(), '[ 6, 7 ]')

    def test_insert3doublerotaterootremoverootheight(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(6)
        x.insert_element(7)
        x.remove_element(7)
        self.assertEqual(x.get_height(), 2)

    def test_insert3doublerotaterightremoveeroottraversals(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(6)
        x.insert_element(7)
        x.remove_element(7)
        self.assertEqual(x.pre_order(), '[ 8, 6 ]')
        self.assertEqual(x.in_order(), '[ 6, 8 ]')
        self.assertEqual(x.post_order(), '[ 6, 8 ]')
















    def test_inserting4andremovingrootrotateheight(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(6)
        x.insert_element(9)
        x.insert_element(5)
        x.remove_element(8)
        self.assertEqual(x.get_height(), 2)


    def test_inserting4andremovingrootrotatetraversals(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(6)
        x.insert_element(9)
        x.insert_element(5)
        x.remove_element(8)
        self.assertEqual(x.pre_order(), '[ 6, 5, 9 ]')
        self.assertEqual(x.in_order(), '[ 5, 6, 9 ]')
        self.assertEqual(x.post_order(), '[ 5, 9, 6 ]')

    def test_inserting5andremovingrootrotateheight(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(6)
        x.insert_element(9)
        x.insert_element(10)
        x.insert_element(5)
        x.remove_element(8)
        self.assertEqual(x.get_height(), 3)


    def test_inserting5andremovingrootrotatetraversals(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(6)
        x.insert_element(9)
        x.insert_element(10)
        x.insert_element(5)
        x.remove_element(8)
        self.assertEqual(x.pre_order(), '[ 9, 6, 5, 10 ]')
        self.assertEqual(x.in_order(), '[ 5, 6, 9, 10 ]')
        self.assertEqual(x.post_order(), '[ 5, 6, 10, 9 ]')

    def test_inserting6andremovingrootrotateheight(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(6)
        x.insert_element(10)
        x.insert_element(11)
        x.insert_element(9)
        x.insert_element(5)
        x.remove_element(8)
        self.assertEqual(x.get_height(), 3)


    def test_inserting6andremovingrootrotatetraversals(self):
        x=self.__BST
        x.insert_element(8)
        x.insert_element(6)
        x.insert_element(10)
        x.insert_element(11)
        x.insert_element(9)
        x.insert_element(5)
        x.remove_element(8)
        self.assertEqual(x.pre_order(), '[ 9, 6, 5, 10, 11 ]')
        self.assertEqual(x.in_order(), '[ 5, 6, 9, 10, 11 ]')
        self.assertEqual(x.post_order(), '[ 5, 6, 11, 10, 9 ]')

    

    
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
            
                
            



if __name__ == '__main__':
    unittest.main()
            