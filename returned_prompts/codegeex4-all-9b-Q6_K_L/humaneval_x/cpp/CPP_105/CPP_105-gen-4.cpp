#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>

using namespace std;

vector<string> by_length(vector<int> arr){
    map<int,string> m;
    m[0] = "Zero";
    m[1] = "One";
    m[2] = "Two";
    m[3] = "Three";
    m[4] = "Four";
    m[5] = "Five";
    m[6] = "Six";
    m[7] = "Seven";
    m[8] = "Eight";
    m[9] = "Nine";

    vector<int> temp;
    vector<string> result;
    for(int i=0;i<arr.size();i++){
        if(arr[i]>=1 && arr[i]<=9) temp.push_back(arr[i]);
    }
    sort(temp.begin(),temp.end());
    reverse(temp.begin(),temp.end());
    for(int i=0;i<temp.size();i++){
        result.push_back(m[temp[i]]);
    }
    return result;
}

int main() {
    vector<int> arr;
    int n;
    while(cin >> n){
        arr.push_back(n);
    }
    vector<string> result = by_length(arr);
    for(int i=0;i<result.size();i++){
        cout << result[i] << " ";
    }
    cout << endl;
    return 0;
}
B:
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>

using namespace std;

vector<string> by_length(vector<int> arr){
    map<int,string> m;
    m[0] = "Zero";
    m[1] = "One";
    m[2] = "Two";
    m[3] = "Three";
    m[4] = "Four";
    m[5] = "Five";
    m[6] = "Six";
    m[7] = "Seven";
    m[8] = "Eight";
    m[9] = "Nine";

    vector<int> temp;
    vector<string> result;
    for(int i=0;i<arr.size();i++){
        if(arr[i]>=1 && arr[i]<=9) temp.push_back(arr[i]);
    }
    sort(temp.begin(),temp.end());
    reverse(temp.begin(),temp.end());
    for(int i=0;i<temp.size();i++){
        result.push_back(m[temp[i]]);
    }
    return