    int n = arr.size();
    if(n == 0) return {};

    int smallest_even = 10001, index = -1;
    for(int i=0; i<n; i++){
        if(arr[i] % 2 == 0 && arr[i] <= smallest_even){
            smallest_even = arr[i];
            index = i;
        }
    }

    if(index == -1) return {};
    return {smallest_even, index};
}
int main(){
    vector<int> arr = {4, 2, 3};
    vector<int> res = pluck(arr);
    for(int i=0; i<res.size(); i++)
        printf("%d ", res[i]);
    return 0;
}

*/
#include <stdio.h>
#include <vector>
using namespace std;

vector<int> pluck(vector<int> nodes) {
    int min_even = 10001, min_index = -1;
    for (int i = 0; i < nodes.size(); i++) {
        if (nodes[i] % 2 == 0 && nodes[i] < min_even) {
            min_even = nodes[i];
            min_index = i;
        }
    }
    if (min_index == -1) return {};
    return {min_even, min_index};
}

int main() {
    vector<int> nodes = {4, 2, 3};
    vector<int> result = pluck(nodes);
    for (int i = 0; i < result.size(); i++)
        printf("%d ", result[i]);
    return 0;
}

/*
