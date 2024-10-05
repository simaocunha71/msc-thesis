    vector<int> res;
    if (lst.empty()) return res;
    sort(lst.begin(), lst.end());
    while (!lst.empty()) {
        res.push_back(lst.front());
        lst.erase(lst.begin());
        if (!lst.empty()) {
            res.push_back(lst.back());
            lst.pop_back();
        }
    }
    return res;
}

int main() {
    vector<int> v = {1, 2, 3, 4};
    vector<int> sorted_v = strange_sort_list(v);
    for(int i=0; i<sorted_v.size(); i++)
        printf("%d ", sorted_v[i]);
    return 0;
}

*/

//C++/Coding Practice/Practice/HackerRank/Problem Solving/Algorithms/Strange Sort/main.cpp
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;

vector<int> strange_sort_vector(vector<int> arr){
    vector<int> result;
    if(arr.empty()) return result;
    sort(arr.begin(), arr.end());
    while(!arr.empty()){
        result.push_back(arr.front());
        arr.erase(arr.begin());
        if(!arr.empty()){
            result.push_back(arr.back());
            arr.pop_back();
        }
    }
    return result;
}

int main() {
    vector<int> v = {1, 2, 3, 4};
    vector<int> sorted_v = strange_sort_vector(v);
    for(int i=0; i<sorted_v.size(); i++)
        printf("%d ", sorted_v[i]);
    return 0;
}

//C++/Coding Practice/Practice/HackerRank/Problem Solving/Algorithms/Strange Sort/main_v2.cpp
#include<std