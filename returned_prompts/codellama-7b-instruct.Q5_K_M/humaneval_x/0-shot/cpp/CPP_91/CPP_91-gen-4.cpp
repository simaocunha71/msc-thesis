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
    int index = 0;
    while (index < S.size())
    {
        if (S[index] == '.' || S[index] == '?' || S[index] == '!')
        {
            index++;
        }
        else
        {
            int start = index;
            while (index < S.size() && S[index] != '.' && S[index] != '?' && S[index] != '!')
            {
                index++;
            }
            if (S.substr(start, index - start).find("I") != string::npos)
            {
                count++;
            }
        }
    }
    return count;
}

