    int cnt = 0, i = 0;
    while (i < S.size()) {
        if (S[i] == 'I') {
            while (S[i] != '.' && S[i] != '?' && S[i] != '!') {
                i++;
            }
            cnt++;
        }
        i++;
    }
    return cnt;
}


/*
You are given a list of strings, and your task is to count the number
of words in this list that are palindromes (read the same forwards and
backwards).

For example:
>>> palindrome_count(["level", "noon", "racecar", "hello"])
3

>>> palindrome_count(["giraffe", "apple", "taco"])
0

Note: You can assume the list will only contain lowercase alphabetical
characters.
*/

int palindrome_count(vector<string> S) {
    int cnt = 0;
    for (int i = 0; i < S.size(); i++) {
        string str = S[i];
        int l = 0, r = str.size() - 1;
        while (l <= r) {
            if (str[l] != str[r]) {
                break;
            }
            l++;
            r--;
        }
        if (l > r) {
            cnt++;
        }
    }
    return cnt;
}


/*
This problem is about a special type of list, called a "doubly linked list".
In a doubly linked list, each node contains two pointers, one to the next
node, and one to the previous node. Here's an example of a doubly linked list:

  1 <=> 2 <=> 3 <=> 4 <=> 5
   ^    ^    ^    ^    ^
  prev prev prev prev prev
   |    |    |    |    |
   4    |    |    |    |
   ^    v    ^    v    ^
  3    1    2    3    4

Here's an example of a doubly linked list