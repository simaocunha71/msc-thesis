    vector<string> result;
    string current_word;
    int word_length=0;
    int vowel_count=0;
    int consonant_count=0;
    for (int i=0;i<s.length();i++)
    {
        char chr=s[i];
        if (chr==' ')
        {
            if (consonant_count==n)
                result.push_back(current_word);
            current_word="";
            word_length=0;
            vowel_count=0;
            consonant_count=0;
        }
        else if (chr=='a'||chr=='e'||chr=='i'||chr=='o'||chr=='u'||chr=='A'||chr=='E'||chr=='I'||chr=='O'||chr=='U')
        {
            vowel_count++;
        }
        else
        {
            consonant_count++;
        }
        current_word+=chr;
        word_length++;
    }
    if (consonant_count==n)
        result.push_back(current_word);
    sort(result.begin(),result.end());
    return result;
} 
} #include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> select_words(string s,int n){
    vector<string> result;
    string current_word;
    int word_length=0;
    int vowel_count=0;
    int consonant_count=0;
    for (int i=0;i<s.length();i++)
    {
        char chr=s[i];
        if (chr==' ')
        {
            if (consonant_count==n)
                result.push_back(current_word);
            current_word="";
            word_length=0;
            vowel_count=0;
            consonant_count=0;
        }
        else if (chr=='a'||chr=='e'||chr=='i'||chr=='o'||chr=='u'||chr=='A'||chr=='E'||chr=='I'||chr=='O'||chr=='U')
        {
            vowel_count++;
        }
        else
        {
            consonant_count++;
        }
        current_word+=chr;
        word_length++;
    }
    if (consonant_count==n)
        result.push_back(current_word);
    sort(result.begin(),result.end());
    return result;
} #include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> select_words(string s,int n){
    vector<string> result;
    string current_word;
    int word_length=0;
    int vowel_count=0;
    int consonant_count=0;
   