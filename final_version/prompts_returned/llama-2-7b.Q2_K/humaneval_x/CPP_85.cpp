/*
Given a non-empty vector of integers lst. add the even elements that are at odd indices..


Examples:
    add({4, 2, 6, 7}) ==> 2 
*/
#include<stdio.h>
#include<vector>
using namespace std;
int add(vector<int> lst){
    int temp = 0;
    for(int i=0; i<lst.size();i++){
        if (lst[i]%2 == 0) temp+=lst[i];
        
    }
    return temp;
}

int main(){
    vector<int> lst={4, 6, 8, -3, 7, 1};
    printf("%d\n", add(lst));
    
   return 0;
}
