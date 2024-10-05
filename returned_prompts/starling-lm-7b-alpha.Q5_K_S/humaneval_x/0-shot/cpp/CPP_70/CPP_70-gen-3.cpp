/*
Given vector of integers, return vector in strange order.
Strange sorting, is when you start with the minimum value,
then maximum of the remaining integers, then minimum and so on.

Examples:
strange_sort_vector({1, 2, 3, 4}) == {1, 4, 2, 3}
strange_sort_vector({5, 5, 5, 5}) == {5, 5, 5, 5}
strange_sort_vector({}) == {}
*/
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> strange_sort_list(vector<int> lst){

    vector<int> ans;
    while(lst.size() > 0){
        int min = *min_element(lst.begin(), lst.end());
        ans.push_back(min);
        lst.erase(find(lst.begin(), lst.end(), min));
        if(lst.size() == 0) break;
        int max = *max_element(lst.begin(), lst.end());
        ans.push_back(max);
        lst.erase