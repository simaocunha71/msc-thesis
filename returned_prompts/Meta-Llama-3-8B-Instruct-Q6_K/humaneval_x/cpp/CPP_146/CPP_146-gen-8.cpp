    int count = 0;
    for(int i = 0; i < nums.size(); i++){
        int n = nums[i];
        if(n > 10 && (n % 10) % 2 != 0 && (n / 10) % 10 % 2 != 0){
            count++;
        }
    }
    return count;
}

int main(){
    vector<int> nums = {15, -73, 14, -15};
    int result = specialFilter(nums);
    cout << result << endl;
    return 0;
}

R:
The solution to the problem is to iterate through the given vector of numbers and check each number against the given conditions. If a number is greater than 10 and both its first and last digits are odd, increment the count. Finally, return the count.

Here is the code in C++:

```cpp
#include <vector>
#include <iostream>

using namespace std;

int specialFilter(vector<int> nums) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        int n = nums[i];
        if (n > 10 && (n % 10) % 2 != 0 && (n / 10) % 10 % 2 != 0) {
            count++;
        }
    }
    return count;
}

int main() {
    vector<int> nums = {15, -73, 14, -15};
    int result = specialFilter(nums);
    cout << result << endl;
    return 0;
}
```

This code defines a function `specialFilter` that takes a vector of integers as input and returns the count of numbers that are greater than 10 and have both first and last digits as odd. The function iterates through the input vector, checks each number against the given conditions, and increments the count if the conditions are met. The `main` function demonstrates the usage of the `specialFilter` function with a sample input vector. The output of the program will be the count of numbers that meet the given conditions.