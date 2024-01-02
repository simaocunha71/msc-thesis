/*
You are given a non-empty vector of positive integers. Return the greatest integer that is greater than 
zero, and has a frequency greater than or equal to the value of the integer itself. 
The frequency of an integer is the number of times it appears in the vector.
If no such a value exist, return -1.
Examples:
    search({4, 1, 2, 2, 3, 1}) == 2
    search({1, 2, 2, 3, 3, 3, 4, 4, 4}) == 3
    search({5, 5, 4, 4, 4}) == -1
*/
#include<stdio.h>
#include<vector>
using namespace std;
int search(vector<int> lst){
    int n = (int)lst.size();
    if(n < 2 ) return -1;
    for(int i=0;i<=n-1;i++) {
        if(lst[i] > 0 && lst[i]*2 >= lst[i+1]){ //i*2 >= sum(i) + n*(i+1)
            return lst[i];
        }else if (n==i+1){
            return -1;
        }
    }
    
}
int main(){
    int a = search({4, 1, 2, 2, 3, 1});
    printf("a == %d", a);
    return 0;
}