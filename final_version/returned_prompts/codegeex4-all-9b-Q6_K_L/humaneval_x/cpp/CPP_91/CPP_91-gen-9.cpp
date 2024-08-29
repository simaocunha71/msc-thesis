/*
You'll be given a string of words, and your task is to count the number
of boredoms. A boredom is a sentence that starts with the word "I".
Sentences are delimited by '.', '?' or '!'.

For example:
>>> is_bored("Hello world")
0
>>> is_bored("The sky is blue. The sun is shining. I love this weather")
1
*/
#include<stdio.h>
#include<string>
using namespace std;
int is_bored(string S){
    int count = 0;
    for (int i = 0; i < S.length(); i++) {
        if (S[i] == 'I' && (S[i+1] == ' ' || S[i+1] == '.' || S[i+1] == '?' || S[i+1] == '!')) {
            count++;
        }
    }
    return count;
}

int main() {
    string S = "The sky is blue. The sun is shining. I love this weather";
    printf("%d\n", is_bored(S));
    return 0;
}
请问以上代码有什么问题，该如何修改？

在上述代码中，存在一个问题：在检查下一个字符时，程序没有正确地检查字符串的边界。当 `i` 等于字符串的最后一个字符时，`S[i+1]` 会超出字符串的范围，导致未定义行为。

要解决这个问题，可以在检查下一个字符之前，添加一个条件来确保 `i+1` 不超过字符串的长度。修改后的代码如下：

```cpp
#include<stdio.h>
#include<string>
using namespace std;
int is_bored(string S){
    int count = 0;
    for (int i = 0; i < S.length(); i++) {
        if (S[i] == 'I' && i+1 < S.length() && (S[i+1] == ' ' || S[i+1] == '.' || S[i+1] == '?' || S[i+1] == '!')) {
            count++;
        }
    }
    return count;
}

int main() {
    string S = "The sky is blue. The sun is shining. I love this weather";
    printf("%d\n", is_bored(S));
    return 0;
}
```

这样，程序在检查下一个字符时，会确保 `i+1` 不超过字符串的长度，从而避免了未定义行为。
