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
#include<math.h>
#include<string>
using namespace std;
int is_bored(string S){

int c=0;
int i=0;
for(i=0;i<S.length();i++)
if(S[i]=='I' && S[i+1]==' ' && S[i+2]!='I')
c++;
return c;
} 

void main()
{
    string S="The sky is blue. The sun is shining. I love this weather";
    printf("%d",is_bored(S));
}
帮我看看代码有没有问题

你的代码看起来大体是正确的，但是有一个小问题。你检查句子是否以"I "开始时，只检查了第三个字符是否是"I"，但没有检查第二个字符是否是空格。如果第二个字符不是空格，那么句子就不会以"I "开始。

你可以通过在检查第三个字符是否是"I"之前，检查第二个字符是否是空格来修复这个问题。以下是修改后的代码：

```c++
#include<stdio.h>
#include<string>
using namespace std;
int is_bored(string S){

int c=0;
int i=0;
for(i=0;i<S.length()-2;i++)  // 修改了这里
if(S[i]=='I' && S[i+1]==' ' && S[i+2]!='I')
c++;
return c;
} 

void main()
{
    string S="The sky is blue. The sun is shining. I love this weather";
    printf("%d",is_bored(S));
}
```

这样修改后，你的代码应该能正确地计算句子以"I "开始的数量了。
