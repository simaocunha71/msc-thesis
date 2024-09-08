#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;

int sum_of_digits(int num){
    int sum = 0;
    if (num < 0) num = -num;
    while(num > 0){
        sum += num % 10;
        num /= 10;
    }
    return sum;
}

vector<int> order_by_points(vector<int> nums){
    int n = nums.size();
    vector<int> index(n);
    for (int i = 0; i < n; i++){
        index[i] = i;
    }
    for (int i = 0; i < n; i++){
        for (int j = i + 1; j < n; j++){
            if (sum_of_digits(nums[i]) > sum_of_digits(nums[j])){
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                temp = index[i];
                index[i] = index[j];
                index[j] = temp;
            }
            else if (sum_of_digits(nums[i]) == sum_of_digits(nums[j])){
                if (index[i] > index[j]){
                    int temp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = temp;
                    temp = index[i];
                    index[i] = index[j];
                    index[j] = temp;
                }
            }
        }
    }
    return nums;
}

int main(){
    vector<int> nums = {1, 11, -1, -11, -12};
    vector<int> sorted_nums = order_by_points(nums);
    for (int i = 0; i < sorted_nums.size(); i++){
        printf("%d ", sorted_nums[i]);
    }
    printf("\n");
    return 0;
}

B:
#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;

int sum_of_digits(int num){
    int sum = 0;
    if (num < 0) num = -num;
    while(num > 0){
        sum += num % 10;
        num /= 10;
    }
    return sum;
}

vector<int> order_by_points(vector<int> nums){
    int n = nums.size();
    vector<int> index(n);
    for (int i = 0; i < n; i++){
        index[i] = i;
    }
    for (int i = 0; i < n;