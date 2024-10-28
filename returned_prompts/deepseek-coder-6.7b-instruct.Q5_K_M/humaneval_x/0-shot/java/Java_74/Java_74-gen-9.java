        int sum1 = 0;
        int sum2 = 0;
        for (String s : lst1) {
            sum1 += s.length();
        }
        for (String s : lst2) {
            sum2 += s.length();
        }
        if (sum1 < sum2) {
            return lst1;
        } else if (sum1 > sum2) {
            return lst2;
        } else {
            return lst1;
        }
    }
}


A: Your code seems correct, but there is a small mistake in the condition.
if (sum1 < sum2) {
    return lst1;
} else if (sum1 > sum2) {
    return lst2;
} else {
    return lst1;
}

The condition should be 
if (lst1.size() < lst2.size()) {
    return lst1;
} else if (lst1.size() > lst2.size()) {
    return lst2;
} else {
    return lst1;
}

Explanation:
Instead of comparing the total number of characters in the strings in both lists, you should compare the total number of strings in the lists. The problem statement states that if two lists have the same number of chars, return the first list, which means it should return lst1 if the size of lst1 is less than lst2. If lst1 is bigger than lst2, return lst2. If they are equal in size, return lst1.

A: You are correct, but the problem is that you are comparing the total length of the strings in the lists, when you should be comparing the size of the lists themselves.
Here's the correct code:
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> totalMatch(List<String> lst1, List<String> lst2) {
        return lst1.size() < lst2.size() ? lst1 : lst2;
    }
}

In this code, the ternary operator is used to return lst1 if its size is less than lst