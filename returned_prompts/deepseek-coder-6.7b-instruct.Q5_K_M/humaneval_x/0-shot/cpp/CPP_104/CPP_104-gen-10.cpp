    vector<int> even_free;
    for(auto num : x){
        bool has_even = false;
        int copy_num = num;
        while(copy_num){
            if((copy_num%10)%2 == 0){
                has_even = true;
                break;
            }
            copy_num /= 10;
        }
        if(!has_even){
            even_free.push_back(num);
        }
    }
    sort(even_free.begin(), even_free.end());
    return even_free;
}

int main() {
    vector<int> x = {15, 33, 1422, 1};
    vector<int> res = unique_digits(x);
    for(int i = 0; i < res.size(); i++)
        printf("%d ", res[i]);
    return 0;
}
```



## Answer Key

```cpp
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

bool hasEvenDigit(int num){
    while(num){
        if((num%10)%2 == 0){
            return true;
        }
        num /= 10;
    }
    return false;
}

vector<int> unique_digits(vector<int> x){
    vector<int> even_free;
    for(auto num : x){
        if(!hasEvenDigit(num)){
            even_free.push_back(num);
        }
    }
    sort(even_free.begin(), even_free.end());
    return even_free;
}

int main() {
    vector<int> x = {15, 33, 1422, 1};
    vector<int> res = unique_digits(x);
    for(int i = 0; i < res.size(); i++)
        printf("%d ", res[i]);
    return 0;
}
```

## Explanation

This code works by first checking if each number in the input vector