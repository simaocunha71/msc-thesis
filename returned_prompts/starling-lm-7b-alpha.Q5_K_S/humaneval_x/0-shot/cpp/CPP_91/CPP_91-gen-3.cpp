    int i=0;
    while(S[i] != '.' && S[i] != '!' && S[i] != '?'){
        i++;
    }
    if(S[0] == 'I'){
        return 1;
    }else{
        return is_bored(S.substr(i));
    }
}





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

    int i=0;
    int c=0;
    while(S[i] != '.' && S[i] != '!' && S[i] != '?'){
        i++;
    }
    if(S[0] == 'I'){
        c++;
    }
    if(i == S.length()){
        return c;
    }
    return c + is_bored(S.substr(i));
}
























































































































































































