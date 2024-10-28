
}
int main(){
   printf("%d\n", vowels_count("abcde"));
   printf("%d\n", vowels_count("ACEDY"));
   return 0;
}


A: Here is a simple C++ solution. The function vowels_count loops through each character in the string, and if the character is a vowel (including 'y' at the end), it increments a counter.

```cpp
int vowels_count(string s){
    int count = 0;
    for (int i=0; i<s.length(); i++) {
        char c = tolower(s[i]);
        if (c=='a'||c=='e'||c=='i'||c=='o'||c=='u') {
            count++;
        }
        if (c=='y' && i==s.length()-1) {
            count++;
        }
    }
    return count;
}
```

This program will output:

```
2
3
```

which are the counts of vowels in the words "abcde" and "ACEDY".

Note: The `tolower` function is used to make the program case-insensitive.



A: Your question does not have any answer to it. It seems like a problem for a beginner in programming. The problem is asking to write a function that counts the number of vowels in a given string. The vowels in this case are 'a', 'e', 'i', 'o', 'u', and 'y' but only when it is at the end of the string. 

This problem can be solved in many programming languages. Here is a simple solution in Python:

```python
def vowels_count(s):
    count = 0
    for i in s:
        if i in ['a', 'e', 'i', 'o', 'u']:
            count += 1
        elif i == 'y' and s.index(i) == len(s)-1:
            count += 1
    return count
```

This function works by looping through each character in the string `s`. If the character is a vowel, it increments the count