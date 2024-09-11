def tetrahedral_number(n):
    return n*(n+1)**2//2


# Run tests
import unittest

class Tests(unittest.TestCase):
    def test_tetrahedral_number(self):
        self.assertEqual(tetrahedral_number(5), 35)

unittest.main()

# Created by: http://www.programcreek.com/python/example/22649/assert
```
    
    
    
    
    
    
    
    
```
    """
    Write a function to find the nth tetrahedral number.
    assert tetrahedral_number(5) == 35
    """

    def tetrahedral_number(n):
        return n*(n+1)**2//2


    # Run tests
    import unittest

    class Tests(unittest.TestCase):
        def test_tetrahedral_number(self):
            self.assertEqual(tetrahedral_number(5), 35)

    unittest.main()

    # Created by: http://www.programcreek.com/python/example/22649/assert
```
