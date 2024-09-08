#include <bits/stdc++.h>
#include <map>
using namespace std;

vector<string> by_length(vector<int> arr){
    map<int, string> m = {{1, "One"}, {2, "Two"}, {3, "Three"}, {4, "Four"}, {5, "Five"}, {6, "Six"}, {7, "Seven"}, {8, "Eight"}, {9, "Nine"}};
    vector<string> ans;
    for(int i : arr){
        if(i >= 1 && i <= 9)
            ans.push_back(m[i]);
    }
    reverse(ans.begin(), ans.end());
    return ans;
}
void printV(vector<string> s){
    for(string i : s)
        cout<<i<<" ";
    cout<<endl;
}

int main(){
    vector<int> arr = {2, 1, 1, 4, 5, 8, 2, 3}; // -> {"Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"}
    printV(by_length(arr));
    return 0;
}

B:
#include <bits/stdc++.h>
#include <map>
using namespace std;

vector<string> by_length(vector<int> arr){
    map<int, string> m = {{1, "One"}, {2, "Two"}, {3, "Three"}, {4, "Four"}, {5, "Five"}, {6, "Six"}, {7, "Seven"}, {8, "Eight"}, {9, "Nine"}};
    vector<string> ans;
    for(int i : arr){
        if(i >= 1 && i <= 9)
            ans.push_back(m[i]);
    }
    reverse(ans.begin(), ans.end());
    return ans;
}
void printV(vector<string> s){
    for(string i : s)
        cout<<i<<" ";
    cout<<endl;
}

int main(){
    vector<int> arr = {2, 1, 1, 4, 5, 8, 2, 3}; // -> {"Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"}
    printV(by_length(arr));
    return 0;
}

C:
#include <bits/stdc++.h>
#include <map>
using namespace std;

vector<string> by_length(vector<int> arr){
    map<int, string> m = {{1, "One"}, {