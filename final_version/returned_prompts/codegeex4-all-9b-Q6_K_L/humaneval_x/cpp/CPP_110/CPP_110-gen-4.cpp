/*
In this problem, you will implement a function that takes two vectors of numbers,
and determines whether it is possible to perform an exchange of elements
between them to make lst1 a vector of only even numbers.
There is no limit on the number of exchanged elements between lst1 and lst2.
If it is possible to exchange elements between the lst1 and lst2 to make
all the elements of lst1 to be even, return "YES".
Otherwise, return "NO".
For example:
exchange({1, 2, 3, 4}, {1, 2, 3, 4}) => "YES"
exchange({1, 2, 3, 4}, {1, 5, 3, 4}) => "NO"
It is assumed that the input vectors will be non-empty.
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string exchange(vector<int> lst1,vector<int> lst2){

    int num1=0;
    int num2=0;
    for(int i=0;i<lst1.size();i++)
    {
        if(lst1[i]%2==0)
            num1++;
    }
    for(int i=0;i<lst2.size();i++)
    {
        if(lst2[i]%2==1)
            num2++;
    }
    if(num2>=num1)
        return "YES";
    else
        return "NO";
}
int main()
{
    vector<int> v={1,2,3,4};
    vector<int> v1={1,2,3,4};
    printf("%s\n",exchange(v,v1).c_str());
    return 0;
}
