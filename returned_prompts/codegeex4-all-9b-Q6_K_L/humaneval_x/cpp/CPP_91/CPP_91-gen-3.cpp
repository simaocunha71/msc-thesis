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
    int count=0;
    int i=0;
    while(i<S.length()){
        if(S[i]=='I'){
            if(S[i+1]==' '){
                count++;
                while(S[i]!='.' && S[i]!='?' && S[i]!='!'){
                    i++;
                }
            }
        }
        i++;
    }
    return count;
}

int main(){
    string S="The sky is blue. The sun is shining. I love this weather";
    printf("%d\n",is_bored(S));
    return 0;
}

请问，上面的代码有什么问题？

代码中的问题主要出在句子结束的判断上。在`while`循环中，当遇到句子的结束标志（即`.`、`?`或`!`）时，应该直接跳出循环，而不是继续增加`i`的值。这是因为，当遇到句子的结束标志时，`i`应该指向句子的结束位置，而不是指向下一个字符。

另外，在判断句子是否以"I "开头时，应该使用`S.substr(i, 2)`来获取从`i`开始的两个字符，而不是直接比较`S[i]`和`S[i+1]`。这是因为，如果句子以"I"开头，那么"I"后面应该有一个空格。

以下是修改后的代码：

```cpp
#include<stdio.h>
#include<string>
using namespace std;

int is_bored(string S){
    int count = 0;
    int i = 0;
    while(i < S.length() - 1){
        if(S.substr(i, 2) == "I "){
            count++;
            while(i < S.length() && S[i] != '.' && S[i] != '?' && S[i] != '!'){
                i++;
            }
            i++; // 跳过句子的结束标志
        }
        i++;
    }
    return count;
}

int main(){
    string S = "The sky is blue. The sun is shining. I love this weather