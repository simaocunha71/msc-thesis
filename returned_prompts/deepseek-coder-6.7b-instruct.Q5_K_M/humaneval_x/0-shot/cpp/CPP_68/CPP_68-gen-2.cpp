    int smallest_even = 10001, index = -1;
    for(int i=0; i<arr.size(); i++){
        if(arr[i] % 2 == 0 && arr[i] <= smallest_even){
            smallest_even = arr[i];
            index = i;
        }
    }
    if(index == -1) return {};
    return {smallest_even, index};
}

int main(){
    vector<int> arr = {4,2,3};
    vector<int> ans = pluck(arr);
    printf("{ %d, %d }", ans[0], ans[1]);
    return 0;
}
*/

#include <iostream>
#include <vector>
#include <climits>
using namespace std;

vector<int> pluck(vector<int> nodes) {
    int min_even = INT_MAX, index = -1;
    for (int i = 0; i < nodes.size(); i++) {
        if (nodes[i] % 2 == 0 && nodes[i] <= min_even) {
            min_even = nodes[i];
            index = i;
        }
    }
    if (index == -1) {
        return {};
    } else {
        return {min_even, index};
    }
}

int main() {
    vector<int> nodes = {4, 2, 3};
    vector<int> result = pluck(nodes);
    if (result.empty()) {
        cout << "{}";
    } else {
        cout << "{ " << result[0] << ", " << result[1] << " }";
    }
    return 0;
}

/*
// 测试用例:
// 输入: {4,2,3}
// 输出: {2, 1}
// 输入: {1,2,3}
// 输出: {2, 1}
// 输入: {}
// 输出: {}
// 输入: {5, 0, 3, 0, 4, 2}
