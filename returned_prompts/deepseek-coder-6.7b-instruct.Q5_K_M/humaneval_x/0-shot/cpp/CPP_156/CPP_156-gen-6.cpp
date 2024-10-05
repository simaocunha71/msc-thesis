  int num[] = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
  string rom[] = {"m","cm","d","cd","c","xc","l","xl","x","ix","v","iv","i"};
  string res = "";

B:
  for(int i=0; i<13; i++){
    while(number>=num[i]){
      res += rom[i];
      number -= num[i];
    }
  }

C:
  return res;
}

int main(){
  printf("%s\n", int_to_mini_roman(19).c_str());
  printf("%s\n", int_to_mini_roman(152).c_str());
  printf("%s\n", int_to_mini_roman(426).c_str());
  return 0;
}
```

Here we have a function int_to_mini_roman which takes a number as input and returns its roman numeral equivalent as a string. We use arrays for the roman numbers and their corresponding integer values. The algorithm iterates over each integer value in the array and whenever the number is greater than or equal to the current integer value, it appends the corresponding roman numeral to the result string and subtracts the integer value from the number. This process continues until the number becomes zero.

Finally the function returns the result string.

The test cases are used to test the function with different integer values.

The time complexity of this function is O(1) as it only iterates over a constant number of elements (13). The space complexity is also O(1) as it uses a constant amount of space to store the integer and roman number arrays and the result string.

The code is written in C++.

The function int_to_mini_roman is not case sensitive. It only converts lowercase numbers to roman numerals.
*/

// C++ program to convert integer to roman numeral

#include <iostream>
#include <string>
using namespace std;

string