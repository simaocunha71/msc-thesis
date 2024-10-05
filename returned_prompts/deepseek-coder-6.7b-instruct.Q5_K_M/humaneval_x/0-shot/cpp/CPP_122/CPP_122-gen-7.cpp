    int sum = 0;
    for(int i=0; i<k; i++){
        if(arr[i]>=1 && arr[i]<=99){
            sum += arr[i];
        }
    }
    return sum;
}

int main(){
    vector<int> arr{111,21,3,4000,5,6,7,8,9};
    int k = 4;
    int result = add_elements(arr,k);
    printf("%d\n",result);
    return 0;
}

*/
#include<stdio.h>
#include<vector>
using namespace std;

int add_elements(vector<int> arr,int k){
    int sum = 0;
    for(int i=0; i<k; i++){
        if(arr[i]>=1 && arr[i]<=99){
            sum += arr[i];
        }
    }
    return sum;
}

int main(){
    vector<int> arr{111,21,3,4000,5,6,7,8,9};
    int k = 4;
    int result = add_elements(arr,k);
    printf("%d\n",result);
    return 0;
}
/*
Output:
24
*/

//Solution:
//The problem asks for the sum of the first k elements from the given array 'arr'. The condition given is that the numbers should have at most two digits.
//The function 'add_elements' takes an integer vector and an integer k as input and returns the sum of the elements which are at most two digits from the first k elements of the vector.
//In the main function, a vector 'arr' and an integer 'k' are defined. The function 'add_elements' is called with 'arr' and 'k' as arguments and the result is printed.
//The result of the program is 24 which is the sum of 21 and 3 which are the first 4 elements of the array 'arr' satisfying the condition.
//The time complexity of this solution is O(k) because we are iterating