In this problem, we are asked to square the elements at indices which are multiples of 3 and cube those at indices which are multiples of 4 and not multiples of 3. The indices start from 0, so the third element will have an index of 2 and the fourth element will have an index of 3. So, we square the third element and cube the fourth element. 

In C++, we can use the modulus operator (%) to check if the index is a multiple of 3 or 4. The modulus operator gives the remainder of the division of the index by 3 or 4. If the remainder is 0, then the index is a multiple of 3 or 4. 

Here is the corrected C++ code:

```cpp
#include<iostream>
#include<vector>
using namespace std;
int sum_squares(vector<int> lst){
    int sum=0;
    for (int i = 0; i < lst.size(); i++){
        if(i%3==0){
            sum += lst[i]*lst[i];
        }
        else if(i%4==0){
            sum += lst[i]*lst[i]*lst