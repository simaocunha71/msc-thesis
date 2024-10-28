    long long sum=0;
    for(int i=0;i<lst.size();i++){
        if(lst[i]>=0 && (int)lst[i]==lst[i] && (int)lst[i]%2==1){
            sum += pow(lst[i],2);
        }
    }
    return sum;
}

*/



#include <stdio.h>
#include <math.h>
#include <stdlib.h>

long long double_the_difference(int* arr, int arr_len){

    long long sum = 0;
    for(int i = 0; i < arr_len; i++){
        if(arr[i] >= 0 && arr[i] % 2 == 1){
            sum += pow(arr[i], 2);
        }
    }
    return sum;
}

int main(){
    int arr[] = {1, 3, 2, 0};
    printf("%lld\n", double_the_difference(arr, 4));  // Output: 10

    int arr1[] = {-1, -2, 0};
    printf("%lld\n", double_the_difference(arr1, 3));  // Output: 0

    int arr2[] = {9, -2};
    printf("%lld\n", double_the_difference(arr2, 2));  // Output: 81

    int arr3[] = {0};
    printf("%lld\n", double_the_difference(arr3, 1));  // Output: 0

    int arr4[] = {};
    printf("%lld\n", double_the_difference(arr4, 0));  // Output: 0

    return 0;
}




































































