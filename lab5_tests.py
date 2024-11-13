import data
import lab5
import unittest

from lab5 import time_add, is_descending, largest_between, furthest_from_origin


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_add1(self):
        t1 = data.Time(5,45,0)
        t2 = data.Time(4,15,0)
        input = time_add(t1,t2)
        expected = data.Time(9,60,0)
        self.assertEqual(input,expected)

    def test_time_add2(self):
        t1 = data.Time(5, 46,30)
        t2 = data.Time(4, 15,12)
        input = time_add(t1, t2)
        expected = data.Time(9, 61,42)
        self.assertEqual(input, expected)



    # Part 4
    def test_is_descending1(self):
        floats = [1.2,4.5,6.7,3.4]
        input = is_descending(floats)
        expected = False
        self.assertEqual(input,expected)

    def test_is_descending2(self):
        floats = [9.7,5.6,4.4,3.2]
        input = is_descending(floats)
        expected = True
        self.assertEqual(input,expected)



    # Part 5
    def test_largest_between1(self):
        nums = [3,4,6,2,5]
        lower = 1
        upper = 4
        input = largest_between(nums,lower,upper)
        expected = 2
        self.assertEqual(input,expected)

    def test_largest_between2(self):
        nums = [8,4,5,3,9]
        lower = 0
        upper = 3
        input = largest_between(nums,lower,upper)
        expected = 0
        self.assertEqual(input,expected)

    # Part 6
    def test_furthest_from_origin1(self):
        p1 = data.Point(3,4)
        p2 = data.Point(4,5)
        p3 = data.Point(6,5)
        input = furthest_from_origin([p1,p2,p3])
        expected = 2
        self.assertEqual(input,expected)

    def test_furthest_from_origin2(self):
        p1 = data.Point(5,4)
        p2 = data.Point(7,6)
        p3 = data.Point(3,5)
        input = furthest_from_origin([p1,p2,p3])
        expected = 1
        self.assertEqual(input,expected)

def groups_of_3(arr: list[int]):
    my_lists = []
    Ubound = len(arr)
    Lbound = 0
    while Lbound < len(arr)-1:
        for i in range(Ubound-Lbound)//3:
            newlist = []
            newlist.append(arr[i])
            my_lists.append(newlist)
        Ubound = Ubound+3
        Lbound = Lbound+3
    return(my_lists)




if __name__ == '__main__':
    unittest.main()
