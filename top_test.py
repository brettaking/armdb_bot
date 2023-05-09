#/usr/bin/python3

import unittest
import top

class TestTopFunctions(unittest.TestCase):

    def test_create_count_list(self):
        self.assertEqual(top.create_count_list(0),[])
        self.assertEqual(top.create_count_list(1), [('Robert De Niro', 12)])
        with self.assertRaises(Exception):
            top.create_count_list('Robert De Niro')
        
    def test_in_movie_check(self):
        self.assertEqual(top.in_movie_check('John Smith'),[])
        self.assertEqual(top.in_movie_check('Julie Andrews'),['The Sound of Music'])
        
    def test_actor_compare(self):
        self.assertEqual(top.actor_compare('Actor One', 'Actor Two'), [])
        self.assertEqual(top.actor_compare('Matt Damon', 'Christian Bale'), ['Ford Vs. Ferrari'])
    
    def test_get_castlist(self):
        self.assertEqual(top.get_castlist('Fake Movie Title'), None)
        self.assertEqual(top.get_castlist('Tremors'), ['Kevin Bacon','Fred Ward','Finn Carter','Michael Gross','Reba McEntire','Bobby Jacoby','Charlotte Stewart','Tony Genaro','Ariana Richards','Richard Marcus'])
        
if __name__ == '__main__':
    unittest.main()