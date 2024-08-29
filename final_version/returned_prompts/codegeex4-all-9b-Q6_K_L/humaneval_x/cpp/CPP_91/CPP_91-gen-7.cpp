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
    int ans = 0;
    int n = S.size();
    for(int i = 0; i < n; i++){
        if(S[i] == 'I' && (S[i+1] == ' ' || S[i+1] == '.' || S[i+1] == '?' || S[i+1] == '!')) ans++;
    }
    return ans;
}
