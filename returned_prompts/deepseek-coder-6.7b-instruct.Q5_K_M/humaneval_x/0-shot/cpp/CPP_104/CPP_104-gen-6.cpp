    vector<int> ans;
    for (auto num : x){
        bool flag = false;
        int temp = num;
        while (temp > 0){
            if ((temp % 10) % 2 == 0){
                flag = true;
                break;
            }
            temp /= 10;
        }
        if (!flag)
            ans.push_back(num);
    }
    sort(ans.begin(), ans.end());
    return ans;
}
int main(){
    vector<int> x = {15, 33, 1422, 1};
    vector<int> res = unique_digits(x);
    for (int i = 0; i < res.size(); i++){
        printf("%d ", res[i]);
    }
    return 0;
}
```

This code checks each number in the input vector. If it doesn't contain any even digit, then it adds it to the result vector. At the end, the result vector is sorted in increasing order and returned.

The time complexity is O(n*m), where n is the length of the input vector and m is the average number of digits in the numbers of the vector. The space complexity is O(n), where n is the length of the input vector.

Please note that this code assumes that the input vector consists of positive integers only.

### Python Solution

```python
# Python solution
def unique_digits(x):
    ans = []
    for num in x:
        if all(int(digit) % 2 != 0 for digit in str(num)):
            ans.append(num)
    return sorted(ans)

x = [15, 33, 1422, 1]
print(unique_digits(x))  # Output: [1, 15, 33]

x = [152, 323, 1422, 10]
print(unique_digits(x))  # Output: []
```

This Python code is almost the same as the C++ code. The `unique_digits` function converts