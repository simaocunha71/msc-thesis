/*
Given a non-empty vector of integers arr and an integer k, return
the sum of the elements with at most two digits from the first k elements of arr.

Example:

    Input: arr = {111,21,3,4000,5,6,7,8,9}, k = 4
    Output: 24 # sum of 21 + 3

Constraints:
    1. 1 <= len(arr) <= 100
    2. 1 <= k <= len(arr)
*/
#include<stdio.h>
#include<vector>
using namespace std;
int add_elements(vector<int> arr,int k){
    int sum=0;
    for (int i = 0 ;i<k;i++){
        int x=arr[i]+arr[i+1];//add the two digits of each element.
        if(x>=10)
            x-=10;
        if(!isdigit(sum))
            sum+=x;
    }
    return sum;
}
int main(){
    int n,k;
    printf("enter the length of array : ");
    scanf("%d",&n);
    printf("enter the number of elements which you want to sum : ");
    scanf("%d",&k);
    vector<int> v(n);//create a vector with n elements.
    for (int i = 0 ;i<n;i++){
        scanf("%d",&v[i]); //read in the array values
    }
    printf("the sum of first two digits with at most k elements is : %d\n",add_elements(v,k));//print the solution.
    return 0;
}
