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
    vector<int> even_odd_cnt(2);//create even and odd counter vectors
    int even[2];
    double remainder;
    for(int i=0;i<10;i++){
        remainder = floor(num / 10.0)/5;
        num %= 10;
        if(remainder == 0){//if we got to the last digit and it is even,then stop the loop
            break;
        }else{
            even[i]++;
        }
    }
    
    return even_odd_cnt;
}
int main(){
   int num = -1234567890;//enter a number and call funciton using that number
   vector<int> v = even_odd_count(num);
   for (int j=0;j<v.size();j++) {
       printf("%d",v[j]);
    }
}