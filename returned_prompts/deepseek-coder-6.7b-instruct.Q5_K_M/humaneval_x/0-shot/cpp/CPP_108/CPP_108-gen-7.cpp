    int count = 0;
    for(int i = 0; i < n.size(); i++){
        int sum = 0;
        if(n[i] < 0){
            while(n[i] != 0){
                sum += n[i] % 10;
                n[i] /= 10;
            }
            if(sum > 0) count++;
        }else{
            while(n[i] != 0){
                sum += n[i] % 10;
                n[i] /= 10;
            }
            if(sum > 0) count++;
        }
    }
    return count;
}


int main(){
    vector<int> v1 = {-1, 11, -11};
    printf("%d", count_nums(v1));
    return 0;
}


A: The problem you are trying to solve is quite simple. You just need to iterate through each number in the vector, and for each number, calculate the sum of its digits. If the sum is greater than 0, then you increment the count.

Here is the solution in C++:

```C++
#include<iostream>
#include<vector>
using namespace std;

int count_nums(vector<int>& nums) {
    int count = 0;
    for(int num : nums) {
        int sum = 0;
        while(num != 0) {
            sum += num % 10;
            num /= 10;
        }
        if(sum > 0) count++;
    }
    return count;
}
```

In this solution, we use a while loop to extract each digit of the number, and add it to the sum. If the sum is greater than 0, we increment the count. At the end, we return the count.

You can test this function with the following code:

```C++
int main() {
    vector<int> nums = {-1, 11, -11};
    cout << count_nums(nums) << endl;  // Output: 1
   