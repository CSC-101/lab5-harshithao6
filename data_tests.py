
import data
import unittest

import lab5


class TestCases(unittest.TestCase):
    #### Time tests
    def test_Time_1(self):
        time = data.Time(7, 20, 1)
        self.assertEqual(7, time.hour)
        self.assertEqual(20, time.minute)
        self.assertEqual(1, time.second)


    def test_Time_2(self):
        time = data.Time(4, 19, 45)
        self.assertEqual(4, time.hour)
        self.assertEqual(19, time.minute)
        self.assertEqual(45, time.second)


    #### Add tests for Time.__eq__
    def test_TimeEqual(self):
        Time1 = (2,30,21)
        Time2 = (4,3,54)
        self.assertNotEqual(Time1,Time2)


    #### Add tests for Time.__repr__
    def test_TimeRepr(self):
       time = data.Time(2,3,50)
       self.assertEqual(repr(time),"Time(2,3,50)")



    #### Point tests
    def test_Point_1(self):
        point = data.Point(7, 20)
        self.assertAlmostEqual(7, point.x)
        self.assertAlmostEqual(20, point.y)


    def test_Point_2(self):
        point = data.Point(4, 19)
        self.assertAlmostEqual(4, point.x)
        self.assertAlmostEqual(19, point.y)


    def test_Point_eq_1(self):
        point1 = data.Point(1, 20)
        point2 = data.Point(1, 20)
        self.assertEqual(point1, point2)


    def test_Point_eq_2(self):
        point1 = data.Point(1, 20)
        self.assertEqual(point1, point1)


    def test_Point_eq_3(self):
        point1 = data.Point(1, 20)
        point2 = data.Point(2, 20)
        self.assertNotEqual(point1, point2)


    def test_Point_eq_4(self):
        point = data.Point(1, 20)
        other = 1.20
        self.assertNotEqual(point, other)


    def test_Point_repr(self):
        point = data.Point(5, 75)
        self.assertEqual('Point(5, 75)', repr(point))

#tests for time_add class
    def test_time_add(self):
        Tim1 = data.Time(5, 3, 36)
        Tim2 = data.Time(4, 2, 60)
        input = lab5.time_add(Tim1,Tim2)
        expected = data.Time(9,6,36)
        print(input)
        print(expected)
        self.assertEqual(input, expected)


#tests for is_decending
    def test_is_descending(self):
        floats = [4.5,6.7,3.2]
        input = lab5.is_descending(floats)
        expected = False
        self.assertEqual(input,expected)


#test for largest_between
    def test_largest_between(self):
        lst = [10, 20, 30, 40, 50]
        lower = 1
        upper = 3
        input = lab5.largest_between(lst,lower,upper)
        expected = 3
        self.assertEqual(input,expected)

    def test2_largest_between(self):
        lst = [30, 15, 60, 75, 54]
        lower = 3
        upper = 2
        input = lab5.largest_between(lst,lower,upper)
        expected = None
        self.assertEqual(input,expected)





#test for furthest_from_origin
    def test_furthest_from_orgin(self):
        points = [data.Point(1, 2), data.Point(3, 4), data.Point(5, 5)]
        input = lab5.furthest_from_origin(points)
        expected = 2
        self.assertEqual(input,expected)

    def test2_furthest_from_orgin(self):
        points = [data.Point(4, 5), data.Point(6, 8), data.Point(4, 5)]
        input = lab5.furthest_from_origin(points)
        expected = 1
        self.assertEqual(input,expected)




if __name__ == '__main__':
    unittest.main()
