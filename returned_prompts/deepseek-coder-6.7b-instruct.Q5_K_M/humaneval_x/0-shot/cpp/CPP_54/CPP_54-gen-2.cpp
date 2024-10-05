    sort(s0.begin(),s0.end());
    sort(s1.begin(),s1.end());
    if(s0==s1)
        return true;
    else
        return false;
}

int main(){
    printf("%d\n",same_chars("eabcdzzzz","dddzzzzzzzddeddabc"));
    printf("%d\n",same_chars("abcd","dddddddabc"));
    printf("%d\n",same_chars("dddddddabc","abcd"));
    printf("%d\n",same_chars("eabcd","dddddddabc"));
    printf("%d\n",same_chars("abcd","dddddddabce"));
    printf("%d\n",same_chars("eabcdzzzz","dddzzzzzzzddddabc"));
    return 0;
}


A: You can use a count array to solve this problem. The count array will keep track of the number of times a character appears in both strings. If the count array for both strings is the same, then the two strings have the same characters.

Here's a Python solution:

```python
def same_chars(s0, s1):
    count0 = [0] * 256
    count1 = [0] * 256
    
    for i in range(len(s0)):
        count0[ord(s0[i])] += 1
    
    for i in range(len(s1)):
        count1[ord(s1[i])] += 1
    
    return count0 == count1
```

In this solution, we first initialize two count arrays, count0 and count1, both with 256 elements (one for each possible ASCII character). We then iterate over each character in the input strings, incrementing the corresponding element in the count arrays. Finally, we return whether the count arrays are equal.

This solution has a time complexity of O(n), where n is the length of the longer input string.

Here's a C++ solution:

```c++
#include <vector>
#include <string>
