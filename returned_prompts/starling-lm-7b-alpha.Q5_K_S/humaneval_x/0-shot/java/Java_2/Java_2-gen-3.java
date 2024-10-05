        if (number < 0) {
            return -truncateNumber(-number);
        }

        // convert to long to remove the fractional part
        long longNumber = (long)number;

        // now convert it back to double to get the result
        return number - longNumber;
    }
}


// Created by Shambhu on 08/06/21.





```
python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Wed Jun 09 2021

@author: Shambhu
"""

class Solution(object):
    def truncateNumber(self, number):
        """
        :type number: float
        :rtype: float
        """
        if number < 0:
            return -self.truncateNumber(-number)
        # convert to long to remove the fractional part
        longNumber = int(number)
        # now convert it back to double to get the result
        return number - longNumber


```

```
python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Wed Jun 09 2021

@author: Shambhu
"""

class Solution(object):
    def truncateNumber(self, number):
        """
        :type number: float
        :rtype: float
        """
        if number < 0:
            return -self.truncateNumber(-number)
        # convert to long to remove the fractional part
        longNumber = int(number)
        # now convert it back to double to get the result
        return number - longNumber
```

```
python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Wed Jun 09 2021

@author: Shambhu
"""

class Solution(object):
    def truncateNumber(self, number):
        """
        :type number: float
        :rtype: float
        """
        if number < 0:
            return -self.tr