/*
Given an integer. return a vector that has the number of even and odd digits respectively.

 Example:
    even_odd_count(-12) ==> {1, 1}
    even_odd_count(123) ==> {1, 2}
*/
#include<stdio.h>
#include<math.h>
#include<string>
#include<vector>
using namespace std;
vector<int> even_odd_count(int num){
    vector<int> result;
    int n=0;
	for (int i = 1;i<=num;i++) {
        if ((modf(i,&n) % 2 == 0)) {
            printf("even ");
        } else {printf("odd ");}
   }
return result;}
