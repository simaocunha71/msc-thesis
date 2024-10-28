    int n=arr.size();
    int max_index=-1;
    for(int i=n-1;i>0;i--){
        if(arr[i]<arr[i-1]){
            max_index=i;
            break;
        }
    }
    return max_index;
}


int main(){
    vector<int> vec1={1,2,4,3,5};
    vector<int> vec2={1,2,3};
    printf("%d\n",can_arrange(vec1));  // Expected Output: 3
    printf("%d\n",can_arrange(vec2));  // Expected Output: -1
    return 0;
}



*/

/*

This function works by iterating over the input vector from right to left.
For each element, it checks if it is less than the element immediately
preceding it. If it is, then it breaks the loop and returns the current
index. If no such element is found after the loop, it returns -1.

*/

// } Driver Code Ends

//{ Driver Code Starts.

#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++

class Solution {
  public:
    int can_arrange(vector<int>& arr) {
        int n = arr.size();
        int max_index = -1;
        for(int i=n-1; i>0; i--) {
            if(arr[i] < arr[i-1]) {
                max_index = i;
                break;
            }
        }
        return max_index;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<int> arr(n);
        for(int i=0;i<n;i++){
            cin>>arr[i];
        }
        Solution ob;
        cout<<ob.can