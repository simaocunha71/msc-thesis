#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool is_prime(int n)
{
    if (n <= 1)
        return false;
    if (n == 2)
        return true;
    if (n % 2 == 0)
        return false;
    for (int i = 3; i * i <= n; i += 2)
    {
        if (n % i == 0)
            return false;
    }
    return true;
}

string words_in_sentence(string sentence)
{
    string result;
    string word;
    int i = 0;
    while (i < sentence.size())
    {
        if (sentence[i] == ' ')
        {
            if (is_prime(word.size()))
            {
                result += word + " ";
            }
            word = "";
        }
        else
        {
            word += sentence[i];
        }
        i++;
    }
    if (is_prime(word.size()))
    {
        result += word;
    }
    return result;
}

int main()
{
    string sentence1 = "This is a test";
    string sentence2 = "lets go for swimming";

    cout << "Input: " << sentence1 << "\nOutput: " << words_in_sentence(sentence1) << endl;
    cout << "Input: " << sentence2 << "\nOutput: " << words_in_sentence(sentence2) << endl;

    return 0;
}


B:
#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool is_prime(int n)
{
    if (n <= 1)
        return false;
    if (n == 2)
        return true;
    if (n % 2 == 0)
        return false;
    for (int i = 3; i * i <= n; i += 2)
    {
        if (n % i == 0)
            return false;
    }
    return true;
}

string words_in_sentence(string sentence)
{
    string result;
    string word;
    int i = 0;
    while (i < sentence.size())
    {
        if (sentence[i] == ' ')
        {
            if (is_prime(word.size()))
            {
                result += word + " ";
            }
            word = "";
        }
        else
        {
            word += sentence[i];
        }
        i++;
    }
    if (is_prime(word.size()))
    {
        result += word;
    }
    return result