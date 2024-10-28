
In the given problem, we need to change the numerical base of the input number to the desired base. The function change_base takes two arguments, x (input number) and base (desired base). It returns a string representation of the converted number.

To solve the problem, we can follow these steps:

1. Define a function called change_base that takes two arguments, x and base.
2. Inside the function, we check if x is divisible by base. If it is, we recursively call the function with x divided by base. This step is necessary to convert the number to its desired base.
3. After the recursive call, we convert the remainder of x divided by base to a string using the to_string function. This step gives us the rightmost digit of the converted number.
4. We concatenate the string representation of the remainder with the result of the recursive call to get the converted number.
5. In the main function, we read the input values of x and base from the user using scanf.
6. We call the change_base function with the input values and print the result using cout.

The time complexity of this solution is O(log(x)), where x is the input number. This is because we need to perform the division and modulo operations log(x) times to convert the number to its desired base. The space complexity is O(log(x)), as we need to store the intermediate results during the conversion process.

Here is the code for the solution:

```cpp
#include<stdio.h>
#include<string>
using namespace std;
string change_base(int x,int base){

    if(x/base){
        return change_base(x/base,base)+to_string(x%base);
    } else {
        return to_string(x);
    }
}
int main(){
    int x,base;
