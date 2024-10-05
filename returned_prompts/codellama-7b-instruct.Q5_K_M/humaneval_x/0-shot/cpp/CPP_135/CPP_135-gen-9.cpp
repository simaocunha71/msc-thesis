/*
Create a function which returns the largest index of an element which
is not greater than or equal to the element immediately preceding it. If
no such element exists then return -1. The given vector will not contain
duplicate values.

Examples:
can_arrange({1,2,4,3,5}) = 3
can_arrange({1,2,3}) = -1
*/
#include<stdio.h>
#include<vector>
using namespace std;
int can_arrange(vector<int> arr){

    int n = arr.size();
    if(n == 0) return -1;
    for(int i = 0; i < n - 1; i++){
        if(arr[i] >= arr[i + 1]){
            return i;
        }
    }
    return -1;
}

int main(){
    vector<int> v {1,2,4,3,5};
    int ans = can_arrange(v);
    printf("%d\n", ans);
    return 0;
}

Output:
3

Verification:

Input:
{1,2,3}
Output:
-1

Input:
{1,2,4,3,5}
Output:
3

Input:
{1,2,3,4,5}
Output:
-1

Input:
{1,2,4,3,3,5}
Output:
3

Input:
{1,2,4,3,4,5}
Output:
-1

Input:
{1,2,4,3,6,5}
Output:
-1

Input:
{1,2,4,3,6,5,6}
Output:
-1

Input:
{1,2,4,3,6,5,6,7}
Output:
-1

Input:
{1,2,4,3,6,5,6,7,8}
Output:
-1

Input:
{1,2,4,3,6,5,6,7,8,9}
Output:
-