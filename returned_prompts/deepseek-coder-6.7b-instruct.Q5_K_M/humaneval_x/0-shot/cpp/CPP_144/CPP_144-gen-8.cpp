    int num1,den1,num2,den2,common_den;
    size_t pos = x.find("/");
    num1 = stoi(x.substr(0, pos));
    den1 = stoi(x.substr(pos + 1));
    pos = n.find("/");
    num2 = stoi(n.substr(0, pos));
    den2 = stoi(n.substr(pos + 1));
    common_den = den1 * den2;
    return ((num1 * den2) == (num2 * den1));
}

int main() {
   printf("%d\n", simplify("1/5", "5/1"));
   printf("%d\n", simplify("1/6", "2/1"));
   printf("%d\n", simplify("7/10", "10/2"));
   return 0;
}

Answer:
The function simplify first converts the input fractions to their simplest form by finding their greatest common divisor (GCD). Then, it checks if the multiplied numerators are equal to the multiplied denominators. If they are, then the fractions are equivalent and the function returns true. Otherwise, it returns false.

Here is the corrected code:

```cpp
#include<stdio.h>
#include<string>
using namespace std;

int gcd(int a, int b) {
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

bool simplify(string x,string n){
    int num1,den1,num2,den2;
    size_t pos = x.find("/");
    num1 = stoi(x.substr(0, pos));
    den1 = stoi(x.substr(pos + 1));
    pos = n.find("/");
    num2 = stoi(n.substr(0, pos));
    den2 = stoi(n.substr(pos + 1));

    int common_den = den1 * den2 / gcd(den1, den2);

    num1 *= common_den / den1;
    num2