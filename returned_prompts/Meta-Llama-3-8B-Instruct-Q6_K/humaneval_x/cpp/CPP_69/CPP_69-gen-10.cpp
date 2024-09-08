    int n = lst.size();
    for(int i=1; i<=n; i++){
        int count = 0;
        for(int j=0; j<n; j++){
            if(lst[j] == i){
                count++;
            }
        }
        if(count >= i){
            return i;
        }
    }
    return -1;
}

int main(){
    vector<int> lst = {4, 1, 2, 2, 3, 1};
    printf("%d\n", search(lst));
    return 0;
}

Output:
2
*/



C++ Program to Find the Greatest Integer with Frequency Greater than or Equal to the Integer Itself:
```c
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int search(vector<int> lst) {
    int n = lst.size();
    int max_freq = -1;
    int max_num = -1;

    for (int i = 1; i <= n; i++) {
        int count = 0;
        for (int j = 0; j < n; j++) {
            if (lst[j] == i) {
                count++;
            }
        }
        if (count >= i && i > max_num) {
            max_num = i;
            max_freq = count;
        }
    }

    if (max_freq >= max_num) {
        return max_num;
    } else {
        return -1;
    }
}

int main() {
    vector<int> lst = {4, 1, 2, 2, 3, 1};
    cout << search(lst) << endl;
    return 0;
}
```

Output:
```
2
```
Explanation:
The program iterates through each integer `i` from 1 to `n`, where `n` is the size of the input vector `lst`. For each `i`, it counts the frequency of `i` in the vector using a nested loop. If the frequency of `i` is greater than or equal to `i` and `i` is greater than the current maximum number, it updates the maximum number and its frequency. Finally, it returns the maximum number if its frequency is greater than or equal to the number itself, otherwise, it returns -1.

In the example, the input vector is `{4, 1, 2, 2, 3, 1}`. The program iterates through each integer `i`