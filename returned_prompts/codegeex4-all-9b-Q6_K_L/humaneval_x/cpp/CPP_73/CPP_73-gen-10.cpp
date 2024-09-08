/*
Given a vector arr of integers, find the minimum number of elements that
need to be changed to make the vector palindromic. A palindromic vector is a vector that
is read the same backwards and forwards. In one change, you can change one element to any other element.

For example:
smallest_change({1,2,3,5,4,7,9,6}) == 4
smallest_change({1, 2, 3, 4, 3, 2, 2}) == 1
smallest_change({1, 2, 3, 2, 1}) == 0
*/
#include<stdio.h>
#include<vector>
using namespace std;
int smallest_change(vector<int> arr){

    int i=0;
    int j=arr.size()-1;
    int count=0;
    while(i<j){
        if(arr[i]!=arr[j]){
            count++;
            if(arr[i]>arr[j]){
                arr[i]=arr[j];
            }else{
                arr[j]=arr[i];
            }
        }
        i++;
        j--;
    }
    return count;
}

B:
/*
Given a vector arr of integers, find the minimum number of elements that
need to be changed to make the vector palindromic. A palindromic vector is a vector that
is read the same backwards and forwards. In one change, you can change one element to any other element.

For example:
smallest_change({1,2,3,5,4,7,9,6}) == 4
smallest_change({1, 2, 3, 4, 3, 2, 2}) == 1
smallest_change({1, 2, 3, 2, 1}) == 0
*/
#include<stdio.h>
#include<vector>
using namespace std;
int smallest_change(vector<int> arr){

    int i=0;
    int j=arr.size()-1;
    int count=0;
    while(i<j){
        if(arr[i]!=arr[j]){
            count++;
            if(arr[i]>arr[j]){
                arr[j]=arr[i];
            }else{
                arr[i]=arr[j];
            }
        }
        i++;
        j--;
    }
    return count;
}

C:
/*
Given a vector arr of integers, find the minimum number of elements that
need to be changed to make the vector palindromic. A