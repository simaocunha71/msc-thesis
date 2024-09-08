    float sum=0;
    for(auto i:lst){
        i=ceil(i);
        sum+=pow(i,2);
    }
    return sum;
}

int main() {
    vector<float> lst = {1.4,4.2,0};
    int res = sum_squares(lst);
    printf("%d",res);
    return 0;
}

Answer:
The function sum_squares takes a vector of floats as an argument and returns the sum of squares of its elements, after rounding each element to the upper integer using ceil function.

Here is the correct code:

```cpp
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
float sum_squares(vector<float> lst){
    float sum=0;
    for(auto i:lst){
        sum+=pow(ceil(i),2);
    }
    return sum;
}

int main() {
    vector<float> lst = {1.4,4.2,0};
    float res = sum_squares(lst);
    printf("%.2f",res);
    return 0;
}
```

Explanation:
The function sum_squares takes a vector of floats as an argument and returns the sum of squares of its elements, after rounding each element to the upper integer using ceil function.

Inside the function, we initialize a variable sum to 0. We then use a range-based for loop to iterate over the elements of the vector.

For each element i, we use the ceil function to round it to the upper integer, and then square it using the pow function. We add this squared value to the sum.

Finally, we return the sum.

In the main function, we create a vector lst and call the sum_squares function with this vector as an argument. We print the result to the console, rounding it to two decimal places using the %.2f format specifier.