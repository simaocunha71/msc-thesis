/*
You are given a string representing a sentence,
the sentence contains some words separated by a space,
and you have to return a string that contains the words from the original sentence,
whose lengths are prime numbers,
the order of the words in the new string should be the same as the original one.

Example 1:
    Input: sentence = "This is a test"
    Output: "is"

Example 2:
    Input: sentence = "lets go for swimming"
    Output: "go for"

Constraints:
    * 1 <= len(sentence) <= 100
    * sentence contains only letters
*/
#include<stdio.h>
#include<string>
using namespace std;
string words_in_sentence(string sentence){
    string output;
    string word;
    int i=0;
    while(i<sentence.length()){
        if(sentence[i]==' '){
            i++;
        }
        else{
            word="";
            while(i<sentence.length()&&sentence[i]!=' '){
                word+=sentence[i];
                i++;
            }
            if(is_prime(word.length())){
                output+=word+' ';
            }
        }
    }
    return output;
}

bool is_prime(int n){
    if(n<=1){
        return false;
    }
    for(int i=2;i*i<=n;i++){
        if(n%i==0){
            return false;
        }
    }
    return true;
}
int main(){
    string sentence;
    cin>>sentence;
    string output=words_in_sentence(sentence);
    cout<<output;
}
请问代码有什么问题？能否改正？

这段代码的主要问题是，在`words_in_sentence`函数中，当找到一个单词时，它并没有检查这个单词是否是句子中的最后一个单词。因此，当句子以一个单词结束而不是以空格结束，函数就会产生错误。例如，如果输入的句子是"This is a test"，函数会在单词"test"后添加一个空格，这会导致输出错误。

此外，`is_prime`函数并没有正确地处理输入为1的情况。在`is_prime`函数中，当输入为1时，函数应该返回`false`，但是实际上返回的是`true`。

以下是修正后的代码：

```cpp
#include<stdio.h>
#include<string>
using namespace std;
string words_in_sentence(string sentence){
    string output;
    string word;
    int i=0;
    while(i<sentence.length()){
        if(sentence[i]==' '){
            i++;
        }
        else{
            word="";
            while(i<sentence.length