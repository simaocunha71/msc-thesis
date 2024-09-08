#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
bool isConsonant(char c)
{
    return (c >= 'a' && c <= 'z') && (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u');
}
int countConsonants(string str)
{
    int count = 0;
    for (int i = 0; i < str.length(); i++)
    {
        if (isConsonant(str[i]))
        {
            count++;
        }
    }
    return count;
}
vector<string> select_words(string s,int n){
    vector<string> result;
    string word = "";
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == ' ')
        {
            if (countConsonants(word) == n)
            {
                result.push_back(word);
            }
            word = "";
        }
        else
        {
            word += s[i];
        }
    }
    if (countConsonants(word) == n)
    {
        result.push_back(word);
    }
    return result;
}
int main()
{
    vector<string> words = select_words("Mary had a little lamb", 4);
    for (string word : words)
    {
        cout << word << endl;
    }
    return 0;
}

B:
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
bool isConsonant(char c)
{
    return (c >= 'a' && c <= 'z') && (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u');
}
int countConsonants(string str)
{
    int count = 0;
    for (int i = 0; i < str.length(); i++)
    {
        if (isConsonant(str[i]))
        {
            count++;
        }
    }
    return count;
}
vector<string> select_words(string s,int n){
    vector<string> result;
    string word = "";
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == ' ')
        {
            if (countConsonants(word) == n)
            {
                result.push_back(word);
            }
            word = "";
       