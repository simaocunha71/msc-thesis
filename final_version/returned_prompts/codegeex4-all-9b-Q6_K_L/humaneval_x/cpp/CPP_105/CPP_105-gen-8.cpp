#include<stdio.h>
#include<vector>
#include<string>
#include<map>
#include<algorithm>
using namespace std;
vector<string> by_length(vector<int> arr){

    vector<string> names = {"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
    map<int, string> map_names;
    for (int i = 0; i < names.size(); i++)
        map_names.insert(pair<int, string>(i + 1, names[i]));
    map<int, int> m;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] >= 1 && arr[i] <= 9)
            m[arr[i]]++;
    }
    vector<string> result;
    for (auto it = m.rbegin(); it != m.rend(); it++)
        for (int i = 0; i < it->second; i++)
            result.push_back(map_names[it->first]);
    return result;
}

