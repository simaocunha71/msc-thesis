
Your Q3 is wrong. You are truncating the number to the integer part and returning the difference between the original number and the integer part, which is not the decimal part of the number. You are using the wrong function to truncate the number to the integer part. You should use the floor function to truncate the number to the integer part, and then subtract the result from the original number to get the decimal part. Here is the correct solution:

```cpp
#include<stdio.h>
#include<math.h>
using namespace std;
float truncate_number(float number){
    return number - floor(number);
}
```

Your Q4 is also wrong. You are checking if the array is sorted in non-decreasing order, but you are not considering the right shift operation. You should check if the array is sorted in non-decreasing order after performing the right shift operation. Here is the correct solution:

```cpp
#include<stdio.h>
#include<vector>
using namespace std;
bool move_one_ball(vector<int> arr){
    int i, j;
    int n = arr.size();
    for (i = 0; i < n; i++) {
        for (j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                return false;
            }
        }
    }
    return true;
}
```