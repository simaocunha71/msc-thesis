/*
You are given two intervals,
where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
The given intervals are closed which means that the interval (start, end)
includes both start and end.
For each given interval, it is assumed that its start is less or equal its end.
Your task is to determine whether the length of intersection of these two 
intervals is a prime number.
Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
which its length is 1, which not a prime number.
If the length of the intersection is a prime number, return "YES",
otherwise, return "NO".
If the two intervals don't intersect, return "NO".


{input/output} samples:
intersection({1, 2}, {2, 3}) ==> "NO"
intersection({-1, 1}, {0, 4}) ==> "NO"
intersection({-3, -1}, {-5, 5}) ==> "YES"
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string intersection( vector<int> interval1,vector<int> interval2){

// solution 1
// int a=0,b=0;
// if(interval1[0]>interval2[0]){
//     a=interval1[0];
//     b=interval2[1];
// }
// else{
//     a=interval2[0];
//     b=interval1[1];
// }
// if(a>b)
//     return "NO";
// if((b-a+1)%2==0)
//     return "NO";
// for(int i=3;(i<=b-a+1)&&(b-a+1>2);i+=2){
//     if((b-a+1)%i==0)
//         return "NO";
// }
// return "YES";

// solution 2
// int a=0,b=0;
// if(interval1[0]>interval2[0]){
//     a=interval1[0];
//     b=interval2[1];
// }
// else{
//     a=interval2[0];
//     b=interval1[1];
// }
// if(a>b)
//     return "NO";
// if((b-a+1)%2==0)
//     return "NO";
// for(int i=3;(i<=b-a