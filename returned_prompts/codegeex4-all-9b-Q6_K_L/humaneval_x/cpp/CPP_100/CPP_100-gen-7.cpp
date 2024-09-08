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

    vector<int> res;
    int curr = n;
    while(curr > 0){
        res.push_back(curr);
        if(n % 2 == 0){
            curr -= 2;
        }else{
            curr -= 1;
        }
    }
    return res;
}
/*
Test cases:
make_a_pile(3) = {3, 5, 7}
make_a_pile(5) = {5, 7, 9, 11, 13}
make_a_pile(8) = {8, 10, 12, 14, 16, 18, 20, 22}
make_a_pile(10) = {10, 12, 14, 16, 18, 20, 22, 24, 26, 28}
make_a_pile(15) = {15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43}
*/

C:
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

    vector<int> res;
    int curr = n;
    while(curr > 0){
        res.push