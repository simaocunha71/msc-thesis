    return arr;
}

int main(){
    vector<int> a = {1, 5, 2, 3, 4};
    vector<int> b = {1, 0, 2, 3, 4};
    vector<int> c = {-2, -3, -4, -5, -6};
    for(auto i : sort_array(a)){
        printf("%d ",i);
    }
    printf("\n");
    for(auto i : sort_array(b)){
        printf("%d ",i);
    }
    printf("\n");
    for(auto i : sort_array(c)){
        printf("%d ",i);
    }
    printf("\n");
    return 0;
}

E:
[1, 2, 3, 4, 5] [0, 1, 2, 3, 4] [-6, -5, -4, -3, -2]
S:
Your task is to implement the sort_array function, which takes a vector of non-negative integers and returns a sorted vector based on the number of ones in their binary representation in ascending order. For similar numbers of ones, the vector should be sorted based on their decimal value.

To solve this problem, you can follow these steps:

1. Create a lambda function that takes an integer and returns a pair. The first element of the pair should be the number of ones in the binary representation of the integer, and the second element should be the integer itself.
2. Use the sort function from the algorithm library to sort the vector based on the lambda function.
3. Return the sorted vector.

Here is the implementation of the sort_array function:

```cpp
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;

vector<int> sort_array(vector<int> arr){
    auto count_ones = [](int n) {
        int count = 0;
        while (n > 0) {
            count += n % 2;
            n /= 2;
        }
        return make_pair(count, n);
    };
    sort(arr.begin(), arr.end(), [](int a, int b) {
        auto pa = count_ones(a);
        auto pb = count_ones(b);
        if (pa.first == pb.first) {
            return pa.second < pb.second;
        }
        return pa.first < pb.first;
    });
    return arr;
}

int main(){
    vector<int> a = {1, 5, 