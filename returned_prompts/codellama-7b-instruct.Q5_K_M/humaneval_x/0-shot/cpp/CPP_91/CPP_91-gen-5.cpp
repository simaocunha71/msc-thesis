/*
You'll be given a string of words, and your task is to count the number of boredoms. A boredom is a sentence that starts with the word "I". Sentences are delimited by '.', '?' or '!'.

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
    int n=0,i=0;
    while(i<S.size()){
        if(S[i]=='.'||S[i]=='?'||S[i]=='!'){
            if(S[i-1]=='I')
                n++;
            i++;
        }
        else
            i++;
    }
    return n;
}
