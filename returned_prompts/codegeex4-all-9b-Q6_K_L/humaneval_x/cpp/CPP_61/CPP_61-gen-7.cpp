/*
Write a function, `correct_bracketing`, that takes a string of '(' and ')'.  The function should return true if every opening bracket has a corresponding closing bracket.  Otherwise, it should return false.

Write a function, `correct_bracketing`, that takes a string of '(' and ')'.  The function should return true if every opening bracket has a corresponding closing bracket.  Otherwise, it should return false.

>>> correct_bracketing("(")
false
>>> correct_bracketing("()")
true
>>> correct_bracketing("(()())")
true
>>> correct_bracketing(")(()")
false

Starter code:

```
#include<stdio.h>
#include<string>
using namespace std;
bool correct_bracketing(string brackets){
    
}
```
*/

bool correct_bracketing(string brackets){
    int count = 0;
    for (int i = 0; i < brackets.length(); i++){
        if (brackets[i] == '('){
            count++;
        }else if (brackets[i] == ')'){
            count--;
        }
        if (count < 0){
            return false;
        }
    }
    return count == 0;
}
int main(){
    printf("%d\n", correct_bracketing("(")); //false
    printf("%d\n", correct_bracketing("()")); //true
    printf("%d\n", correct_bracketing("(()())")); //true
    printf("%d\n", correct_bracketing(")(()")); //false
    return 0;
}
