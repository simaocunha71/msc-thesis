    if(strings.size()==0)
        return "None";
    string longest_word;
    for(int i=0;i<strings.size();i++)
    {
        if(longest_word.length()<strings[i].length())
            longest_word = strings[i];
    }
    return longest_word;
}





/*
Given a number, return a vector of its divisors. For example, the divisors of 8 are {1, 2, 4, 8}.

>>> divisors(21)
[1, 3, 7, 21]

>>> divisors(36)
[1, 2, 3, 4, 6, 9, 12, 18, 36]
*/
#include<iostream>
#include<vector>
using namespace std;

vector<int> divisors(int number){
    vector<int> divs;
    for(int i=1;i<=number;i++)
    {
        if(number%i==0)
            divs.push_back(i);
    }
    return divs;
}







/*
Given a number, return a vector of its prime factors. For example, the prime factors of 8 are {2, 2, 2}.

>>> prime_factors(21)
[3, 7]

>>> prime_factors(36)
[2, 2, 3]
*/
#include<iostream>
#include<vector>
using namespace std;

vector<int> prime_factors(int number){
    vector<int> divs = divisors(number);
    vector<int> primes;
    for(int i=0;i<divs.size();i++)
    {
        int d = divs[i];
        bool is_prime = true;
        for(int j=2;j*j<=d;j++)
        {
            if(d%j==0)
            {
                is_prime = false;
                break;
            }
        }
