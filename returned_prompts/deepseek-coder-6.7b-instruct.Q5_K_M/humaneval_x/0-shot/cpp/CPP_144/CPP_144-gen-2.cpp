    int num1, den1, num2, den2;
    sscanf(x.c_str(), "%d/%d", &num1, &den1);
    sscanf(n.c_str(), "%d/%d", &num2, &den2);

    return (num1 * den2) % (den1 * num2) == 0;
}

int main(){
    printf("%d\n", simplify("1/5", "5/1"));
    printf("%d\n", simplify("1/6", "2/1"));
    printf("%d\n", simplify("7/10", "10/2"));
    return 0;
}

Explanation:
In this program, I have used the sscanf() function which is used for extracting formatted input from a string. The function sscanf() reads the input from a string and stores them in the specified variables. 
In the given problem, the string is being converted to integer format. The variables num1, den1 are storing the numerator and denominator of string x and num2, den2 are storing the numerator and denominator of string n.
The function then returns true if the product of num1 and num2 is equal to the product of den1 and den2. If not, it returns false.

The main() function is used to test the simplify() function by passing various inputs.
*/


A: Here is a simple C++ solution:

```cpp
#include <iostream>
#include <sstream>
using namespace std;

bool simplify(string x, string n) {
    istringstream issx(x), issn(n);
    int num1, den1, num2, den2;
    char slash;

    if (!(issx >> num1 >> slash >> den1) || !(issn >> num2 >> slash >> den2)) {
        return false;
    }

    return (num1*num2) % (den1*den2) == 0;
}

int main() {
    cout << simplify("1/5", "5/1") << endl;  // true, output 1
    cout << simplify("1/