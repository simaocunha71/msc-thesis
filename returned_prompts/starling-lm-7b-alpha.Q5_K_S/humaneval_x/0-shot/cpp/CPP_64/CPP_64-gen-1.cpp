    int c=0;
    for(int i=0;i<s.length();i++){
        if((s[i]=='a')||(s[i]=='e')||(s[i]=='i')||(s[i]=='o')||(s[i]=='u')||(s[i]=='y' && i==s.length()-1)){
            c++;
        }
    }
    return c;
}


/*
Write a function max_sum_subarray which takes a string as input and returns the maximum sum of a subarray of the input string. 

A subarray is a contiguous part of a string. For example, if the input string is "abcde", the following are all subarrays of the string: "a", "ab", "abc", "abcd", "abcde", "b", "bc", "bcde", "cd", "cde", "de". 

In this problem, the input string is an array of characters. The sum of a subarray is the sum of all the characters in the subarray. For example, if the input string is "1 2 3 4 5", the sum of the subarray "2 3 4" is 9. 

Here is an example to help you understand better: 

>>> max_sum_subarray("1 2 3 4 5 6 7 8 9")
16
>>> max_sum_subarray("1 -2 3 4 -5")
9
>>> max_sum_subarray("10 20 30 40 50")
100

In the first example, the maximum sum subarray is "6 7 8". In the second example, the maximum sum subarray is "3 4". In the third example, the maximum sum subarray is all the numbers in the string.

Note that a subarray can be empty too, and in that case, the sum of the subarray is 0.

Here is how you can use the function:

>>> max_sum_subarray("1 2 -3 4 -5 6")
11

To implement the function, you can