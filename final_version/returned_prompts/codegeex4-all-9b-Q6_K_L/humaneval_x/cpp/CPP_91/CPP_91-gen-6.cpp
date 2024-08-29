#include<stdio.h>
#include<string>
#include<stdlib.h>
using namespace std;
int is_bored(string S){
    int count=0;
    string sentence="";
    for(int i=0;i<S.size();i++)
    {
        if(S[i]=='.'||S[i]=='?'||S[i]=='!'){
            if(sentence[0]=='I')
            {
                count++;
                sentence="";
            }
            else
            {
                sentence="";
            }
        }
        else
        {
            sentence+=S[i];
        }

    }

    return count;
} 
B:
#include<stdio.h>
#include<string>
using namespace std;
int is_bored(string S){

    int count=0;
    string sentence="";
    for(int i=0;i<S.size();i++)
    {
        if(S[i]=='.'||S[i]=='?'||S[i]=='!'){
            if(sentence[0]=='I')
            {
                count++;
                sentence="";
            }
            else
            {
                sentence="";
            }
        }
        else
        {
            sentence+=S[i];
        }

    }

    return count;
} 
C:
#include<stdio.h>
#include<string>
using namespace std;
int is_bored(string S){
    int count=0;
    string sentence="";
    for(int i=0;i<S.size();i++)
    {
        if(S[i]=='.'||S[i]=='?'||S[i]=='!'){
            if(sentence[0]=='I')
            {
                count++;
                sentence="";
            }
            else
            {
                sentence="";
            }
        }
        else
        {
            sentence+=S[i];
        }

    }

    return count;
}
D:
#include<stdio.h>
#include<string>
#include<stdlib.h>
using namespace std;
int is_bored(string S){
    int count=0;
    string sentence="";
    for(int i=0;i<S.size();i++)
    {
        if(S[i]=='.'||S[i]=='?'||S[i]=='!'){
            if(sentence[0]=='I')
            {
                count++;
                sentence="";
            }
            else
            {
                sentence="";
            }
        }
        else
        {
            sentence+=S[i];
        }

    }

    return count;
}
E:
#include<stdio.h>
#include<string>
using namespace std;
int is_bored(string S){

    int count=0;
    string sentence="";
    for(int i=0;i<S.size();i++)
    {
        if(S[i]=='.'||S[i]=='?'||S[i]=='!