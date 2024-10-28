    int result = 1;
    int sum = 0;
    if(arr.empty()){
        return -32768;
    }
    for(int i=0;i<arr.size();i++){
        if(arr[i]>0){
            result *= 1;
        }
        else if(arr[i]<0){
            result *= -1;
        }
        else{
            return 0;
        }
        sum += abs(arr[i]);
    }
    return result*sum;
}
*/

// C++ program
#include<bits/stdc++.h>
using namespace std;

int prod_signs(vector<int> arr){
    int result = 1;
    int sum = 0;
    if(arr.empty()){
        return -32768;
    }
    for(int i=0;i<arr.size();i++){
        if(arr[i]>0){
            result *= 1;
        }
        else if(arr[i]<0){
            result *= -1;
        }
        else{
            return 0;
        }
        sum += abs(arr[i]);
    }
    return result*sum;
}

int main(){
    // test the function
    vector<int> arr = {1, 2, 2, -4};
    cout<<prod_signs(arr)<<endl; // output: -9

    vector<int> arr2 = {0, 1};
    cout<<prod_signs(arr2)<<endl; // output: 0

    vector<int> arr3 = {};
    cout<<prod_signs(arr3)<<endl; // output: -32768
    return 0;
}
```









































































