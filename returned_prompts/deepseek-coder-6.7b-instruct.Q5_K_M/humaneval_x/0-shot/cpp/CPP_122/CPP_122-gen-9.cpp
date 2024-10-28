    int sum = 0;
    for(int i=0; i<k; i++){
        if(arr[i]<10 || arr[i]>=100){
            sum += arr[i];
        }
    }
    return sum;
}

int main(){
    vector<int> arr = {111,21,3,4000,5,6,7,8,9};
    int k = 4;
    printf("%d\n",add_elements(arr,k));
    return 0;
}

*/

//Python Version:

def add_elements(arr, k):
    sum = 0
    for i in range(k):
        if arr[i]<10 or arr[i]>=100:
            sum += arr[i]
    return sum

arr = [111,21,3,4000,5,6,7,8,9]
k = 4
print(add_elements(arr,k))

//C++ Version:

#include<bits/stdc++.h>
using namespace std;

int add_elements(vector<int> arr,int k){
    int sum = 0;
    for(int i=0; i<k; i++){
        if(arr[i]<10 || arr[i]>=100){
            sum += arr[i];
        }
    }
    return sum;
}

int main(){
    vector<int> arr = {111,21,3,4000,5,6,7,8,9};
    int k = 4;
    cout<<add_elements(arr,k)<<endl;
    return 0;
}

//Python Version:

def add_elements(arr, k):
    sum = 0
    for i in range(k):
        if arr[i]<10 or arr[i]>=100:
            sum += arr[i]
    return sum

arr = [111,21,3,4000,5,6,7,8,9]
k