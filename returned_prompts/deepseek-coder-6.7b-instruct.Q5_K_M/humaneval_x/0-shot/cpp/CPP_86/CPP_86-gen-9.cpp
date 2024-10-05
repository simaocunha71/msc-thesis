    string result = "";
    size_t pos = 0;
    while(pos < s.size()){
        if(s[pos] == ' '){
            result += ' ';
            pos++;
        }
        else{
            string temp = "";
            while(pos < s.size() && s[pos] != ' '){
                temp += s[pos];
                pos++;
            }
            sort(temp.begin(), temp.end());
            result += temp;
        }
    }
    return result;
}
int main(){
    string s = "Hello World!!!";
    printf("%s\n", anti_shuffle(s).c_str());
    return 0;
}
*/

#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

void anti_shuffle(char* s){
    char* word[100];
    int count = 0;
    char* pch = strtok(s, " ");
    while(pch != NULL){
        word[count] = pch;
        count++;
        pch = strtok(NULL, " ");
    }
    for(int i = 0; i < count; i++){
        sort(word[i], word[i] + strlen(word[i]));
    }
    for(int i = 0; i < count; i++){
        printf("%s ", word[i]);
    }
    printf("\n");
}
int main(){
    char s[] = "Hello World!!!";
    anti_shuffle(s);
    return 0;
}
*/

#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string anti_shuffle(string s)
{
    string result = "";
    size_t pos = 0;
    while(pos < s.size())
    {
        if(s[pos] == ' ')
        {
            result += ' ';
            pos++;
        }
        else
        {
            string temp = "";
            while(pos < s.