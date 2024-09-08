    vector<int> res;
    res.push_back(3);
    if(n == 0)
        return res;
    res.push_back(1);
    if(n == 1)
        return res;
    res.push_back(2);
    if(n == 2)
        return res;
    for(int i = 3; i <= n; i++){
        if(i % 2 == 0){
            res.push_back(1 + i/2);
        }else{
            res.push_back(res[i-1] + res[i-2] + res[i-3]);
        }
    }
    return res;
}

int main(){
    int n = 3;
    vector<int> res = tri(n);
    for(int i = 0; i < res.size(); i++){
        printf("%d ", res[i]);
    }
    printf("\n");
    return 0;
}

B:
The Tribonacci sequence is defined as the following recurrence relation:
tri(1) = 3
tri(2) = 1
tri(n) = 1 + n / 2, if n is even.
tri(n) =  tri(n - 1) + tri(n - 2) + tri(n - 3), if n is odd.
Here is a C++ implementation of the function tri(int n) that returns the first n + 1 numbers of the Tribonacci sequence:
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> tri(int n) {
    vector<int> res;
    res.push_back(3);
    if(n == 0)
        return res;
    res.push_back(1);
    if(n == 1)
        return res;
    res.push_back(2);
    if(n == 2)
        return res;
    for(int i = 3; i <= n; i++){
        if(i % 2 == 0){
            res.push_back(1 + i/2);
        }else{
            res.push_back(res[i-1] + res[i-2] + res[i-3]);
        }
    }
    return res;
}

int main() {
    int n = 3;
    vector<int> res = tri(n);
    for(int i = 0; i < res.size(); i++){
        cout << res[i] << " ";
    }
    cout << endl;
    return 0;
}
```
This code uses a vector to store the Tribonacci sequence,