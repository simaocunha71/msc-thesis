    int changes = 0;
    int n = arr.size();
    for(int i = 0; i <= n/2; i++){
        if(arr[i] != arr[n-i-1]){
            changes++;
        }
    }
    return changes;
}

int main(){
    vector<int> arr = {1, 2, 3, 2, 1};
    printf("%d\n", smallest_change(arr));
    return 0;
}

*/

#include<iostream>
#include<vector>
using namespace std;
int smallest_change(vector<int> arr){
    int changes = 0;
    int n = arr.size();
    for(int i = 0; i <= n/2; i++){
        if(arr[i] != arr[n-i-1]){
            changes++;
        }
    }
    return changes;
}

int main(){
    vector<int> arr = {1, 2, 3, 2, 1};
    cout << smallest_change(arr) << endl;
    return 0;
}

//C++/HackerRank/Arrays/HourGlass.cpp
/*
