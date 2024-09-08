You can solve this problem by iterating over the input array and keep track of the product of the signs and the sum of the magnitudes of the integers. If a number is negative, multiply the product of the signs by -1. Then return the product of the signs multiplied by the sum of the magnitudes.

Here is the C++ code for the problem:

```cpp
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;

int prod_signs(vector<int> arr){
    if(arr.empty())return -32768;
    int sign=1;
    int sum=0;
    for(int i=0;i<arr.size();i++){
        if(arr[i]<0)sign*=-1;
        sum+=abs(arr[i]);
    }
    return sign*sum;
}

int main()
{
    vector<int> arr={1,2,2,-4};
    printf("%d",prod_signs(arr));
    return 0;
}
```

In this code, we first check if the input array is empty. If it is, we return -32768 as per the problem statement. Then we initialize two variables, sign and sum, to 1 and 0 respectively. We iterate over the array, and for each number, we check if it is negative. If it is, we multiply the sign by -1. We then add the absolute value of the number to the sum. Finally, we return the product of the signs multiplied by the sum.

The output of this code will be -9, which is the correct answer for the input array {1,2,2,-4}. The product of the signs is -1, and the sum of the magnitudes is 9, so the product of the signs multiplied by the sum of the magnitudes is -9.