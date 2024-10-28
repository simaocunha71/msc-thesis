/*
Create a function that returns a vector (a, b), where "a" is
the largest of negative integers, and "b" is the smallest
of positive integers in a vector.
If there is no negative or positive integers, return them as 0.

Examples:
largest_smallest_integers({2, 4, 1, 3, 5, 7}) == {0, 1}
largest_smallest_integers({}) == {0,0}
largest_smallest_integers({0}) == {0,0}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> largest_smallest_integers(vector<int> lst){

    vector<int> result={0,0};
    if(lst.size()==0) return result;
    if(lst.size()==1) return result={lst[0],lst[0]};
    int a=0;
    int b=0;
    for(int i