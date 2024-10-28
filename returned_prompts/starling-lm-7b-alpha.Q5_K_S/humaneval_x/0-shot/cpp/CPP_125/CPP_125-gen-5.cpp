    vector<string> res;
    for(int i = 0; i < txt.size(); i++)
    {
        if(txt[i] == ' ' || txt[i] == ',')
        {
            res.push_back(txt.substr(0,i));
            txt = txt.substr(i+1);
        }
    }
    if(txt.size() != 0) res.push_back(txt);
    return res;
}

/*
Given a number, return the sum of all the divisors of that number that are also prime.
Examples
sum_divisors(12) ➞ 17
Explanations: The divisors of 12 are 1, 2, 3, 4, 6 and 12. The prime divisors are 2, 3, and 11. The sum of these is 17.
sum_divisors(28) ➞ 27
Explanations: The divisors of 28 are 1, 2, 4, 7, 14 and 28. The prime divisors are 7 and 13. The sum of these is 27.
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
int sum_divisors(int num)
{
    int res = 0;
    for(int i = 2; i <= num; i++)
    {
        if(num % i == 0 && is_prime(i)) res += i;
    }
    return res;
}

/*
Given a string of alphanumeric characters, return a string of all the vowels in the string, in order
Examples
vowel_string("Hello World") ➞ "eo"
Explanations: The vowels in "Hello World" are e, o.
vowel_string("This is a test") ➞ "iiae"
Explanations: The vowels in "This is a test" are i, a, e.
*/
#include<stdio.h