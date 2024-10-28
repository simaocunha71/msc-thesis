    vector<string> v;
    int count=0;
    string word;
    for(int i=0;i<txt.length();i++){
        if(txt[i]==' '||txt[i]==','){
            if(word.length()>0){
                v.push_back(word);
                word="";
            }
        }else{
            if(txt[i]>='a'&&txt[i]<='z'){
                if((txt[i]-'a')%2==1) count++;
            }
            word+=txt[i];
        }
    }
    if(word.length()>0){
        v.push_back(word);
    }
    else if(count>0){
        v.push_back(to_string(count));
    }
    return v;
}

int main() {
    vector<string> v = split_words("Hello,world!");
    for(int i=0;i<v.size();i++){
        printf("%s ",v[i].c_str());
    }
    printf("\n");
    return 0;
}

*/


A: Your code is correct and it should work as expected. It splits the input string into words (either by whitespace or comma), counts the number of lower-case letters with odd order in the alphabet and pushes these into the vector. If there's nothing to split, it just pushes the count into the vector.
Here is the code snippet for your question:

```cpp
#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

vector<string> split_words(string txt){
    vector<string> v;
    int count=0;
    string word;
    for(int i=0;i<txt.length();i++){
        if(txt[i]==' '||txt[i]==','){
            if(word.length()>0){
                v.push_back(word);
                word="";
            }
        }else{
           