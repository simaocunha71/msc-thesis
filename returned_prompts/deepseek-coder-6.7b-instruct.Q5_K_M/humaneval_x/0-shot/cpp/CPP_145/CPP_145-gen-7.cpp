    int sum = 0, i, j, temp, min_index;
    vector<int> result(nums.size());
    for(i=0; i<nums.size(); i++){
        sum = 0;
        temp = abs(nums[i]);
        while(temp){
            sum += temp%10;
            temp /= 10;
        }
        result[i] = (nums[i]<0)?-sum:sum;
    }

    for(i=0; i<nums.size()-1; i++){
        min_index = i;
        for(j=i+1; j<nums.size(); j++){
            if(result[j] < result[min_index]){
                min_index = j;
            }
        }
        temp = result[i];
        result[i] = result[min_index];
        result[min_index] = temp;

        temp = nums[i];
        nums[i] = nums[min_index];
        nums[min_index] = temp;
    }
    return nums;
}

int main(){
    vector<int> nums = {1, 11, -1, -11, -12};
    vector<int> sorted_nums = order_by_points(nums);
    for(int i=0; i<sorted_nums.size(); i++){
        printf("%d ", sorted_nums[i]);
    }
    return 0;
}

This is a C++ solution.

The function `order_by_points` takes a vector of integers as input.
It calculates the sum of digits for each number, and then stores the
sum with the sign of the original number. The sum of digits is negative
if the original number is negative.

Then it sorts the vector using selection sort algorithm.

In the main function, we call this function with a vector of integers,
and print the sorted vector.
*/
```

## C++ Solution

```cpp
#include<vector>
#include<algorithm>
#include<cmath>
