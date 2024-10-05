    int balance = 0;
    for (int i=0; i<operations.size(); i++) {
        balance += operations[i];
        if (balance < 0) {
            return true;
        }
    }
    return false;
}








/*
You are given two strings s1 and s2 and an integer n. You need to check whether s1 is a substring of s2 or not. But you are not allowed to use substring function or any other built-in functions to check this.

You can only use the following operations:

1. Compare two characters c1 and c2. If c1==c2, return true. Else, return false.
2. Get the character at index i from s1 or s2. To get the character at index i in s1, you can use s1[i]. Similarly, to get the character at index i in s2, you can use s2[i].
3. Increment the index i by 1.

Here is a sample implementation that passes all test cases:

// Returns true if s1 is a substring of s2, else returns false
bool isSubstring(char s1[], char s2[], int n) {
    int i = 0, j = 0;
    while (s1[i] && s2[j]) {
        if (s1[i] == s2[j]) {
            i++;
            j++;
        } else {
            i = 0;
            j++;
        }
    }
    return s1[i] == '\0';
}

The function works as follows:

1. It starts by comparing the first character of s1 and s2. If they are equal, it increments both i and j by 1. Otherwise, it resets i to 0 and increments j by 1. It continues doing this until either s1 or s2 is exhausted.

2. If s1 is exhausted (i.e. s1[i] == '\0'), then s1 is a substring of s2 and it returns true. Otherwise, it returns false.

*/



















