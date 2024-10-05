    int i,j,k;
    for(i=0;i<l.size();i++)
    for(j=i+1;j<l.size();j++)
    for(k=j+1;k<l.size();k++)
    if(l[i]+l[j]+l[k]==0)
    return true;
    return false;
}
```

## 2. C++
```cpp
#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

// Question 1
bool has_close_elements(vector<float> numbers, float threshold) {
    sort(numbers.begin(), numbers.end());
    for (int i = 0; i < numbers.size() - 1; i++) {
        if (abs(numbers[i] - numbers[i + 1]) < threshold) {
            return true;
        }
    }
    return false;
}

// Question 2
vector<string> separate_paren_groups(string paren_string) {
    vector<string> result;
    string temp = "";
    int level = 0;
    for (char c : paren_string) {
        if (c == '(') {
            level++;
            temp += c;
        }
        if (c == ')') {
            level--;
            temp += c;
            if (level == 0) {
                result.push_back(temp);
                temp = "";
            }
        }
    }
    return result;
}

// Question 3
float truncate_number(float number) {
    return number - int(number);
}

// Question 4
bool triples_sum_to_zero(vector<int> l) {
    sort(l.begin(), l.end());
    for (int i = 0; i < l.size() - 2; i++) {
        int j = i + 1;
        int k = l.size() - 1;
        while (j < k) {
            if (l[i] +