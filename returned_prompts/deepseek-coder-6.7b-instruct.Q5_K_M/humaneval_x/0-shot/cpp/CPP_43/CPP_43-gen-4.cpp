    int n=l.size();
    sort(l.begin(),l.end());
    int i=0,j=n-1;
    while(i<j){
        if(l[i]+l[j]>0)
            j--;
        else if(l[i]+l[j]<0)
            i++;
        else
            return true;
    }
    return false;
}
int main(){
    vector<int> l{2, 4, -5, 3, 5, 7};
    printf("%s",pairs_sum_to_zero(l)?"True":"False");
    return 0;
}
*/

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int compare(const void * a, const void * b) {
    return (*(int*)a - *(int*)b);
}

bool pairs_sum_to_zero(int* arr, int arr_size){
    qsort(arr, arr_size, sizeof(int), compare);
    int i = 0;
    int j = arr_size - 1;
    while(i < j) {
        if (arr[i] + arr[j] > 0) {
            j--;
        } else if (arr[i] + arr[j] < 0) {
            i++;
        } else {
            return true;
        }
    }
    return false;
}

int main(){
    int arr[] = {2, 4, -5, 3, 5, 7};
    int arr_size = sizeof(arr) / sizeof(arr[0]);
    printf("%s", pairs_sum_to_zero(arr, arr_size) ? "True" : "False");
    return 0;
}

//C++/main.cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool pairs_sum_to_zero(vector<int> l){
    int n = l.size();
    sort(l.begin(),l.