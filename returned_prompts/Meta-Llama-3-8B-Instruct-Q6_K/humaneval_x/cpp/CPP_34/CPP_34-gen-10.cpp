    vector<int> unique;
    set<int> s;
    for(int i = 0; i < l.size(); i++){
        s.insert(l[i]);
    }
    for(set<int>::iterator it = s.begin(); it != s.end(); it++){
        unique.push_back(*it);
    }
    return unique;
}

int main(){
    vector<int> l = {5, 3, 5, 2, 3, 3, 9, 0, 123};
    vector<int> result = unique(l);
    for(int i = 0; i < result.size(); i++){
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
}
//Output: 0 2 3 5 9 123
```
Here's a more concise way to do it using `std::set` and `std::vector`:
```c++
#include <vector>
#include <set>
#include <algorithm>

std::vector<int> unique(std::vector<int> v) {
    std::set<int> s(v.begin(), v.end());
    std::vector<int> result(s.begin(), s.end());
    return result;
}
```
This code uses the `std::set` container to remove duplicates from the input vector, and then uses the `std::vector` constructor to create a new vector from the set. This is a more efficient and concise way to achieve the same result.