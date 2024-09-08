#include <bits/stdc++.h>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
vector<string> by_length(vector<int> arr){
    vector<string> result;
    if (arr.size() == 0) return result;
    map<int, string> map = {
        {1, "One"},
        {2, "Two"},
        {3, "Three"},
        {4, "Four"},
        {5, "Five"},
        {6, "Six"},
        {7, "Seven"},
        {8, "Eight"},
        {9, "Nine"}
    };
    sort(arr.begin(), arr.end());
    reverse(arr.begin(), arr.end());
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] >= 1 && arr[i] <= 9) result.push_back(map[arr[i]]);
    }
    return result;
}

B:
#include <bits/stdc++.h>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
vector<string> by_length(vector<int> arr){
    vector<string> result;
    if (arr.size() == 0) return result;
    map<int, string> map = {
        {1, "One"},
        {2, "Two"},
        {3, "Three"},
        {4, "Four"},
        {5, "Five"},
        {6, "Six"},
        {7, "Seven"},
        {8, "Eight"},
        {9, "Nine"}
    };
    sort(arr.begin(), arr.end());
    reverse(arr.begin(), arr.end());
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] >= 1 && arr[i] <= 9) result.push_back(map[arr[i]]);
    }
    return result;
}

C:
#include <bits/stdc++.h>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
vector<string> by_length(vector<int> arr){
    vector<string> result;
    if (arr.size() == 0) return result;
    map<int, string> map = {
        {1, "One"},
        {2, "Two"},
        {3, "Three"},
        {4, "Four"},
        {5, "Five"},
        {6, "Six"},
        {7, "Seven"},
        {8, "Eight"},
        {9, "Nine"}
    };
    sort