    vector<int> res;
    for(int i=0;i<x.size();i++){
        bool flag=true;
        int num=x[i];
        while(num>0){
            int digit=num%10;
            if(digit%2==0){
                flag=false;
                break;
            }
            num=num/10;
        }
        if(flag) res.push_back(x[i]);
    }
    sort(res.begin(),res.end());
    return res;
}

int main(){
    vector<int> x={15,33,1422,1};
    vector<int> y=unique_digits(x);
    for(int i=0;i<y.size();i++){
        printf("%d ",y[i]);
    }
    return 0;
}

Answer:
In the above code, we traverse through each element in the input vector `x`. For each element, we check if it has any even digit. If it doesn't, we add it to our result vector `res`. Finally, we sort the result vector and return it.

Here is the code:

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> unique_digits(vector<int> x) {
    vector<int> res;
    for (int i = 0; i < x.size(); i++) {
        bool flag = true;
        int num = x[i];
        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                flag = false;
                break;
            }
            num = num / 10;
        }
        if (flag) res.push_back(x[i]);
    }
    sort(res.begin(), res.end());
    return res;
}

int main() {
    vector<int> x = {15, 33, 1422, 1};
    vector<int> y = unique_digits(x);
    for (int i = 0; i < y.size(); i++) {
        cout << y[i] << " ";
    }
    return 0;
}
```

Output:

```
1 15 33
```



In this code, we first define a function `unique_digits` that takes a vector of integers as input and returns a sorted vector of integers that do not have any even digits. In the `main` function, we create a vector `x` containing the numbers 15, 33, 1422, and 1. We then call the `unique_digits` function with