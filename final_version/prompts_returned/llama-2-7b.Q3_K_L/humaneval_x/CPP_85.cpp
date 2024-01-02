/*
Given a non-empty vector of integers lst. add the even elements that are at odd indices..


Examples:
    add({4, 2, 6, 7}) ==> 2 
*/
#include<stdio.h>
#include<vector>
using namespace std;
int add(vector<int> lst){
    int n=lst.size();
    for (int i =1; i <n/2+1 ;i++ ){
        if(!(lst[i]% 2))
            lst[i]=lst[i]+lst[(i-1)% n];
            
    }
     return lst;
}
main(){
    vector<int> v={4, 2, 6, 7};
   add(v);
}