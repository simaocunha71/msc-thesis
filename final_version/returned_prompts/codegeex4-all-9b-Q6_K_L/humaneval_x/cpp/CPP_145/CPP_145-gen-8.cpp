```cpp
#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;
vector<int> order_by_points(vector<int> nums){
    //计算每个数字的位数
    vector<int> digit_sum;
    for(int i = 0; i < nums.size(); i++){
        int sum = 0;
        int num = abs(nums[i]);
        while(num != 0){
            sum += num % 10;
            num /= 10;
        }
        digit_sum.push_back(sum);
    }

    //根据位数对数字进行排序
    for(int i = 0; i < nums.size() - 1; i++){
        for(int j = 0; j < nums.size() - 1 - i; j++){
            if(digit_sum[j] > digit_sum[j+1]){
                int temp = nums[j];
                nums[j] = nums[j+1];
                nums[j+1] = temp;

                int temp_sum = digit_sum[j];
                digit_sum[j] = digit_sum[j+1];
                digit_sum[j+1] = temp_sum;
            }
        }
    }

    return nums;
}
```
这段代码首先计算每个数字的位数，然后根据位数对数字进行排序。但是，这段代码的时间复杂度为O(n^2)，其中n是数字的个数。我们可以使用快速排序算法来提高效率。以下是改进后的代码：

```cpp
#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;
vector<int> order_by_points(vector<int> nums){
    //计算每个数字的位数
    vector<int> digit_sum;
    for(int i = 0; i < nums.size(); i++){
        int sum = 0;
        int num = abs(nums[i]);
        while(num != 0){
            sum += num % 10;
            num /= 10;
        }
        digit_sum.push_back(sum);
    }

    //根据位数对数字进行排序
    quicksort(nums, digit_sum, 0, nums.size() - 1);

    return nums;
}

void quicksort(vector<int>& nums, vector<int>& digit_sum, int left, int right){
    if(left >= right){
        return;
    }

    int pivot = digit_sum[left];
    int i = left, j = right;

    while(i < j){
        while(i < j && digit_sum[j] >= pivot){
            j--;
        }
        while(i