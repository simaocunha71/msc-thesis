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
#include<cstring>
using namespace std;
int is_bored(string S){
    int ans=0;
    int n=S.length();
    int i=0;
    int j=0;
    while(i<n){
        j=i;
        if(S[i]=='I' || S[i]=='i'){
            while(j<n && S[j]!='.' && S[j]!='?' && S[j]!='!') j++;
            if(j<n) ans++;
            i=j+1;
        }
        else i++;
    }
    return ans;
}

B:
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
#include<cstring>
using namespace std;
int is_bored(string S){
    int ans=0;
    int n=S.length();
    int i=0;
    int j=0;
    while(i<n){
        j=i;
        if(S[i]=='I' || S[i]=='i'){
            while(j<n && S[j]!='.' && S[j]!='?' && S[j]!='!') j++;
            if(j<n) ans++;
            i=j+1;
        }
        else i++;
    }
    return ans;
}

C:
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
#include<cstring>
using namespace std;
