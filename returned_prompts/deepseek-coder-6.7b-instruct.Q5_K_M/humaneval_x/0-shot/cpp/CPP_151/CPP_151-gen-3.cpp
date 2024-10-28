    long long sum = 0;
    for(int i=0; i<lst.size(); i++){
        if(lst[i]>0 && lst[i]==floor(lst[i]) && lst[i]%2){
            sum += pow(lst[i], 2);
        }
    }
    return sum;
}


int main() {
    vector<float> lst{1, 3, 2, 0};
    printf("%lld\n", double_the_difference(lst)); // 10
    return 0;
}

*/

int main() {
    vector<float> lst{-1, -2, 0};
    printf("%lld\n", double_the_difference(lst)); // 0
    return 0;
}


int main() {
    vector<float> lst{9, -2};
    printf("%lld\n", double_the_difference(lst)); // 81
    return 0;
}


int main() {
    vector<float> lst{0};
    printf("%lld\n", double_the_difference(lst)); // 0
    return 0;
}


int main() {
    vector<float> lst{};
    printf("%lld\n", double_the_difference(lst)); // 0
    return 0;
}
```

---
## C++ Solution
```C++
#include<iostream>
#include<vector>
#include<cmath>
using namespace std;

long long double_the_difference(vector<float> lst){
    long long sum = 0;
    for(int i=0; i<lst.size(); i++){
        if(lst[i]>0 && lst[i]==floor(lst[i]) && lst[i]%2){
            sum += pow(lst[i], 2);
        }
    }
    return sum;
}

int main() {
    vector<float> lst{1,