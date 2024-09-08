    vector<string> result;
    for(int i = 0; i < arr.size(); i++){
        if(arr[i] >= 1 && arr[i] <= 9){
            result.push_back(to_string(arr[i]));
        }
    }
    sort(result.begin(), result.end());
    reverse(result.begin(), result.end());
    map<int, string> m = {{1, "One"}, {2, "Two"}, {3, "Three"}, {4, "Four"}, {5, "Five"}, {6, "Six"}, {7, "Seven"}, {8, "Eight"}, {9, "Nine"}};
    for(int i = 0; i < result.size(); i++){
        result[i] = m[stoi(result[i])];
    }
    return result;
}

int main() {
    vector<int> arr = {2, 1, 1, 4, 5, 8, 2, 3};
    vector<string> result = by_length(arr);
    for(auto i : result) cout << i << " ";
    cout << endl;
    return 0;
}

B:
#include<bits/stdc++.h>
using namespace std;

vector<string> by_length(vector<int> arr) {
    vector<string> res;
    for(int i = 0; i < arr.size(); i++) {
        if(arr[i] >= 1 && arr[i] <= 9) {
            res.push_back(to_string(arr[i]));
        }
    }
    sort(res.begin(), res.end());
    reverse(res.begin(), res.end());
    map<int, string> m = {{1, "One"}, {2, "Two"}, {3, "Three"}, {4, "Four"}, {5, "Five"}, {6, "Six"}, {7, "Seven"}, {8, "Eight"}, {9, "Nine"}};
    for(int i = 0; i < res.size(); i++) {
        res[i] = m[stoi(res[i])];
    }
    return res;
}

int main() {
    vector<int> arr = {2, 1, 1, 4, 5, 8, 2, 3};
    vector<string> res = by_length(arr);
    for(auto i : res) {
        cout << i << " ";
    }
    cout << endl;
    return 0;
}

C:
#include <bits/stdc++.h>
using namespace std;

vector<string> by_length(vector<int