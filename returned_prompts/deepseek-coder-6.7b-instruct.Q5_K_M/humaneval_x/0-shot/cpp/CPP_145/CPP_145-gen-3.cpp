    int i, j, temp, sum, min_index;
    for(i = 0; i < nums.size(); i++){
        min_index = i;
        for(j = i+1; j < nums.size(); j++){
            sum = 0;
            temp = nums[j];
            while(temp != 0){
                sum += abs(temp%10);
                temp /= 10;
            }
            temp = nums[min_index];
            sum = 0;
            while(temp != 0){
                sum += abs(temp%10);
                temp /= 10;
            }
            if(sum < nums[min_index])
                min_index = j;
            else if(sum == nums[min_index] && j < min_index)
                min_index = j;
        }
        if(min_index != i){
            temp = nums[i];
            nums[i] = nums[min_index];
            nums[min_index] = temp;
        }
    }
    return nums;
}
*/

int main()
{
    vector<int> nums = {1, 11, -1, -11, -12};
    vector<int> res;
    res = order_by_points(nums);
    for(int i = 0; i < res.size(); i++)
        printf("%d ",res[i]);
    return 0;
}
```

This code defines a function `order_by_points` which sorts a vector of integers in ascending order based on the sum of their digits. It first calculates the sum of the digits of each number in the vector. If two numbers have the same sum of digits, the one with the smaller index in the original vector comes first. The function returns the sorted vector.

The main function tests the `order_by_points` function with the vector `{1, 11, -1, -11, -12}` and prints the result.
*/

int main()
{
    vector<int> nums = {1, 11,