    vector<int> res;
    for (int i=0; i<x.size(); i++) {
        int num = x[i];
        bool isEvenDigit = false;
        while (num > 0) {
            if ((num % 10) % 2 == 0) {
                isEvenDigit = true;
                break;
            }
            num /= 10;
        }
        if (!isEvenDigit)
            res.push_back(x[i]);
    }
    sort(res.begin(), res.end());
    return res;
}

int main()
{
    vector<int> x = {15, 33, 1422, 1};
    vector<int> res = unique_digits(x);
    for(int i=0; i<res.size(); i++)
        printf("%d ", res[i]);
    printf("\n");
    return 0;
}

*/
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

bool hasEvenDigit(int n) {
    while (n > 0) {
        if ((n % 10) % 2 == 0)
            return true;
        n /= 10;
    }
    return false;
}

vector<int> unique_digits(vector<int> x){
    vector<int> res;
    for (int i=0; i<x.size(); i++) {
        if (!hasEvenDigit(x[i]))
            res.push_back(x[i]);
    }
    sort(res.begin(), res.end());
    return res;
}

int main()
{
    vector<int> x = {15, 33, 1422, 1};
    vector<int> res = unique_digits(x);
    for(int i=0; i<res.size(); i++)
        cout << res[i] << " ";
    cout << "\n";
    return 0;
}
```

## Problem 3

Given a