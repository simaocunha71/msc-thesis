    int m = grid.size(), n = grid[0].size();
    int buckets = 0, total_wells = 0;
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            if(grid[i][j] == 1){
                buckets++;
            }
            total_wells += grid[i][j];
        }
    }
    if(capacity >= total_wells){
        return buckets;
    }

B:
    int fill_levels = 0;
    while(capacity < total_wells){
        total_wells -= buckets;
        fill_levels++;
    }
    return fill_levels;
}

int main() {
    vector<vector<int>> grid = {{0,0,1,0}, {0,1,0,0}, {1,1,1,1}};
    int capacity = 1;
    printf("%d\n", max_fill(grid, capacity));
    return 0;
}

//Q1/main.cpp
#include<iostream>
#include<vector>
#include<algorithm>
#include<unordered_map>
#include<queue>

using namespace std;

//Q1
vector<int> frequencySort(vector<int>& nums) {
    unordered_map<int,int> count;
    priority_queue<pair<int,int>> heap;
    vector<int> res;

    for(int num: nums){
        count[num]++;
    }

    for(auto& it: count){
        heap.push({it.second, it.first});
    }

    while(!heap.empty()){
        int n = heap.top().first;
        int num = heap.top().second;
        heap.pop();
        for(int i = 0; i < n; i++){
            res.push_back(num);
        }
    }
    return res;
}

int main() {
    vector<int> nums = {1,1