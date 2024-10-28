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
    int len = S.length();
    int i = 0;
    while(i < len){
        if(S[i] == '.'){
            i++;
        }
        else if(S[i] == '?' || S[i] == '!'){
            i += 2;
        }
        else if(S[i] == 'I' && S[i + 1] == ' '){
            count++;
        }
        else{
            i++;
        }
    }
    return count;
}
int main(){
    string S;
    cin >> S;
    printf("%d\n", is_bored(S));
    return 0;
}
