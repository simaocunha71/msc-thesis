/*
In this task, you will be given a string that represents a number of apples and oranges 
that are distributed in a basket of fruit this basket contains 
apples, oranges, and mango fruits. Given the string that represents the total number of 
the oranges and apples and an integer that represent the total number of the fruits 
in the basket return the number of the mango fruits in the basket.
for example:
fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
*/
#include<stdio.h>
#include<string>
using namespace std;
int fruit_distribution(string s,int n){

    int i,apples = 0,oranges = 0,mangoes = 0;

    for(i = 0;i<s.length();i++)
    {
        if(s[i] == 'a')
        {
            apples = apples*10 + (s[i+1] - '0');
        }
        if(s[i] == 'o')
        {
            oranges = oranges*10 + (s[i+1] - '0');
        }
        if(s[i] == 'm')
        {
            mangoes = mangoes*10 + (s[i+1] - '0');
        }
    }
    return n-apples-oranges-mangoes;
}
int main(){
    string s;
    int n;
    cin>>s>>n;
    cout<<fruit_distribution(s,n);
    return 0;
}

