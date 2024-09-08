Your task is to write a function that returns true if a number x is a simple power of n and false in other cases.
x is a simple power of n if n**int=x
For example:
is_simple_power(1, 4) => true
is_simple_power(2, 2) => true
is_simple_power(8, 2) => true
is_simple_power(3, 2) => false
is_simple_power(3, 1) => false
is_simple_power(5, 3) => false
*/
#include<stdio.h>
#include<math.h>
using namespace std;
bool is_simple_power(int x,int n){

    int base = ceil(sqrt(x));
    int exp = 0;
    while(base * base <= x){
        if(base * base == x) return true;
        base++;
        exp++;
    }
    return false;
}

int main(){
    printf("%d\n",is_simple_power(1, 4)); //true
    printf("%d\n",is_simple_power(2, 2)); //true
    printf("%d\n",is_simple_power(8, 2)); //true
    printf("%d\n",is_simple_power(3, 2)); //false
    printf("%d\n",is_simple_power(3, 1)); //false
    printf("%d\n",is_simple_power(5, 3)); //false
    return 0;
}
C++


Solution:
This problem can be solved by using a simple mathematical approach. We can start from the square root of the number and check if it is a perfect square. If it is, then we