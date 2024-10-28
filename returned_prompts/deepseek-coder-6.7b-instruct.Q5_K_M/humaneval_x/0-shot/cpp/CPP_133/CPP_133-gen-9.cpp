    int sum = 0;
    for(int i=0; i<lst.size();i++){
        lst[i] = ceil(lst[i]);
        sum += pow(lst[i],2);
    }
    return sum;
}

int main(){
    vector<float> lst = {1.4,4.2,0};
    printf("%d",sum_squares(lst));
    return 0;
}


A: The problem seems to be related with rounding numbers to the upper integer.
The ceil() function will take a double and return the smallest integer not less than the argument.

So, if you have something like 1.4, it will round to 2. The problem with the code is that it is not being applied to each element of the vector, but only to the last one, because it is being applied to the same number for all elements.

The correct code is:
#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

int sum_squares(vector<float> lst){
    int sum = 0;
    for(int i=0; i<lst.size();i++){
        lst[i] = ceil(lst[i]);
        sum += pow(lst[i],2);
    }
    return sum;
}

int main(){
    vector<float> lst = {1.4,4.2,0};
    cout << sum_squares(lst) << endl;
    return 0;
}

This will correctly apply the rounding to each element of the vector.
Hope it helps.

A: The problem is in the line where you apply the ceil function. Right now, you're applying it to the same number for every element in lst. Instead, you should apply it to each individual element in lst. Here is a corrected version of your code:

```cpp
#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

int sum_squares(vector<float> lst){
    int sum = 0;
    for