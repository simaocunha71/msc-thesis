Here is the solution:
```c
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;

int specialFilter(vector<int> nums){
    int count = 0;
    for(int num: nums){
        if(num > 10 && (num % 10) % 2 != 0 && (num / 10) % 10 % 2 != 0){
            count++;
        }
    }
    return count;
}

int main(){
    vector<int> nums = {15, -73, 14, -15};
    printf("The result is: %d\n", specialFilter(nums));
    return 0;
}
```

In the function `specialFilter(vector<int> nums)`, we iterate over each number in the input vector `nums`. For each number, we check three conditions:
1. `num > 10`: The number is greater than 10.
2. `(num % 10) % 2 != 0`: The last digit of the number is odd (1, 3, 5, 7, 9).
3. `(num / 10) % 10 % 2 != 0`: The first digit of the number (after removing the last digit) is odd.

If all three conditions are true, we increment the `count` variable. Finally, we return the `count` variable, which represents the number of elements in the vector that meet the specified conditions.

In the `main` function, we create a vector `nums` with the input numbers, and then call the `specialFilter` function to get the result. We print the result using `printf`. The output will be `1`, which is the number of elements in the vector that meet the specified conditions.