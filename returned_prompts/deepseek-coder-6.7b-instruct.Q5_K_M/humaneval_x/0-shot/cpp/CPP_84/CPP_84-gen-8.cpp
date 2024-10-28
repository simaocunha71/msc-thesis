    int sum=0;
    string binary="";
    while(N>0){
        sum+=N%10;
        N/=10;
    }
    while(sum>0){
        binary=to_string(sum%2)+binary;
        sum/=2;
    }
    return binary;
}
int main(){
    int N;
    printf("Enter the number: ");
    scanf("%d",&N);
    string result = solve(N);
    printf("Sum of digits in binary is: %s\n",result.c_str());
    return 0;
}
*/

#include<bits/stdc++.h>
using namespace std;

string solve(int N){
    int sum=0;
    string binary="";
    while(N>0){
        sum+=N%10;
        N/=10;
    }
    while(sum>0){
        binary=to_string(sum%2)+binary;
        sum/=2;
    }
    return binary;
}

int main(){
    int N;
    printf("Enter the number: ");
    scanf("%d",&N);
    string result = solve(N);
    printf("Sum of digits in binary is: %s\n",result.c_str());
    return 0;
}#include <iostream>
#include <vector>

using namespace std;

vector<int> solve(vector<int> &A, int B) {
    vector<int> ans;
    int n = A.size();
    for(int i=0; i<n; i++) {
        if(A[i] != B) ans.push_back(A[i]);
    }
    return ans;
}

int main() {
    vector<int> A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int B = 5;
    vector<int> res = solve(A, B);
    for(auto i: