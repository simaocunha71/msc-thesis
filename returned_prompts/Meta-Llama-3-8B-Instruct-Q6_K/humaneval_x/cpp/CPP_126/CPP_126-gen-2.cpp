    if(lst.size() <= 1) return true;
    for(int i = 0; i < lst.size() - 1; i++) {
        if(lst[i] > lst[i+1]) return false;
        if(lst[i] == lst[i+1]) return false;
    }
    return true;
}

int main() {
    vector<int> lst1 = {5};
    vector<int> lst2 = {1, 2, 3, 4, 5};
    vector<int> lst3 = {1, 3, 2, 4, 5};
    vector<int> lst4 = {1, 2, 3, 4, 5, 6};
    vector<int> lst5 = {1, 2, 3, 4, 5, 7};
    vector<int> lst6 = {1, 3, 2, 4, 5, 6, 7};
    vector<int> lst7 = {1, 2, 2, 3, 3, 4};
    vector<int> lst8 = {1, 2, 2, 2, 3, 4};

    printf("%d\n", is_sorted(lst1)); //1
    printf("%d\n", is_sorted(lst2)); //1
    printf("%d\n", is_sorted(lst3)); //0
    printf("%d\n", is_sorted(lst4)); //1
    printf("%d\n", is_sorted(lst5)); //1
    printf("%d\n", is_sorted(lst6)); //0
    printf("%d\n", is_sorted(lst7)); //1
    printf("%d\n", is_sorted(lst8)); //0

    return 0;
}
```



Solution:
Here is the solution to the problem:

```c++
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
bool is_sorted(vector<int> lst){
    if(lst.size() <= 1) return true;
    for(int i = 0; i < lst.size() - 1; i++) {
        if(lst[i] > lst[i+1]) return false;
    }
    return true;
}

int main() {
    vector<int> lst1 = {5};
    vector<int> lst2 = {1, 2, 3, 4, 5};
    vector<int> lst3 = {1, 3, 2