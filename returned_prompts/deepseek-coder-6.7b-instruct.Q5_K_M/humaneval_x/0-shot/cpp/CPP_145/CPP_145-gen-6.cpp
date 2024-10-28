
    for (int i = 0; i < nums.size(); i++)
    {
        for (int j = i+1; j < nums.size(); j++)
        {
            int sum_i = 0, sum_j = 0;
            int abs_i = abs(nums[i]);
            int abs_j = abs(nums[j]);

            while (abs_i)
            {
                sum_i += abs_i % 10;
                abs_i /= 10;
            }

            while (abs_j)
            {
                sum_j += abs_j % 10;
                abs_j /= 10;
            }

            if ((sum_i > sum_j) || (sum_i == sum_j && nums[i] > nums[j]))
            {
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
        }
    }

    return nums;
}


int main()
{
    vector<int> v = {1, 11, -1, -11, -12};
    vector<int> sorted_v = order_by_points(v);
    for (int i = 0; i < sorted_v.size(); i++)
    {
        printf("%d ", sorted_v[i]);
    }
    return 0;
}


*/


A: You can solve this problem by using sort function in C++ and a custom comparator.

Here is the C++ code:

```C++
#include <algorithm>
#include <vector>
#include <cmath>

int sum_of_digits(int num){
    num = abs(num);
    int sum = 0;
    while(num){
        sum += num%10;
        num /= 10;
    }
    return sum;
}

bool compare(int a, int b){
    int sum_a = sum_of_digits(a);
    int sum_b = sum_of_