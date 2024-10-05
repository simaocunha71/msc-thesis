    vector<int> even_node;
    for(int i=0; i<arr.size(); i++){
        if(arr[i]%2 == 0){
            even_node.push_back(arr[i]);
        }
    }
    if(even_node.size()==0){
        return {};
    }
    sort(even_node.begin(), even_node.end());
    int smallest_even = even_node[0];
    for(int i=0; i<arr.size(); i++){
        if(arr[i] == smallest_even){
            return {smallest_even, i};
        }
    }
}
int main(){
    vector<int> arr = {5, 0, 3, 0, 4, 2};
    vector<int> res = pluck(arr);
    for(int i=0; i<res.size(); i++){
        printf("%d ",res[i]);
    }
    return 0;
}
*/

// C++ solution of the problem
#include<bits/stdc++.h>
using namespace std;

vector<int> pluck(vector<int> nodes){
    int smallest_even_value = INT_MAX, smallest_even_index = -1;
    for(int i = 0; i < nodes.size(); i++){
        if(nodes[i] % 2 == 0 && nodes[i] <= smallest_even_value){
            smallest_even_value = nodes[i];
            smallest_even_index = i;
        }
    }
    if(smallest_even_index == -1){
        return {};
    }
    return {smallest_even_value, smallest_even_index};
}

// Test cases
int main(){
    vector<int> nodes = {5, 0, 3, 0, 4, 2};
    vector<int> res = pluck(nodes);
    for(int i = 0; i < res.size(); i++){
        cout << res[i] << " ";
    }
    return 0;
}
/*
    This C++