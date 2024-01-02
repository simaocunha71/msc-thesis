/*
Given a positive integer n, you have to make a pile of n levels of stones.
The first level has n stones.
The number of stones in the next level is:
    - the next odd number if n is odd.
    - the next even number if n is even.
Return the number of stones in each level in a vector, where element at index
i represents the number of stones in the level (i+1).

Examples:
>>> make_a_pile(3)
{3, 5, 7}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> make_a_pile(int n){
    vector<int> piles;
    if (n%2 ==1) return piles = {3, 5 ,7};
    int oddnum = 1+((n-1)/2);
    piles.push_back(oddnum);
    return piles;
}
//Driver Code
int main(){
     // your code goes here

     int n=4;
     vector<int> piles = make_a_pile(n);
    for (auto i: piles)
        printf("%d \n",i);
    return 0;
}