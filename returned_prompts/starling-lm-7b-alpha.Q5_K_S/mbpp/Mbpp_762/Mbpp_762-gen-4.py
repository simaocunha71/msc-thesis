def check_monthnumber_number(monthnumber):
    month_list = [4,6,9,11]
    for i in month_list:
        if i == monthnumber:
            return True
    return False

# Here is some test code to check that the function works. Don't change it.
import unittest

class Test(unittest.TestCase):
    def test_check_monthnumber_number(self):
        self.assertEqual(check_monthnumber_number(6), True)
        self.assertEqual(check_monthnumber_number(8), False)

if __name__ == '__main__':
    unittest.main()







"""
Here's a possible solution to the problem. The function takes a month number as input and returns True if the month has 30 days, and False otherwise. The function works by checking if the month number is in the list of months that have 30 days.
"""
```
 
def check_monthnumber_number(monthnumber):
    month_list = [4,6,9,11]
    for i in month_list:
        if i == monthnumber:
            return True
    return False
```
This solution uses a list to store the month numbers that have 30 days (months 4, 6, 9, and 11). The function iterates through this list and checks if the input month number is in the list. If it is, the function returns True. If not, it returns False.

The provided test code uses the unittest module to test the function. It checks that the function returns True for the month number 6 and False for the month number 8, which is not in the list of months with 30 days.
```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```
