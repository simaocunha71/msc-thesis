The solution to this question is to use a stack to keep track of the opening brackets. When we encounter an opening bracket, we push it onto the stack. When we encounter a closing bracket, we check if the stack is empty. If it is, then there is no corresponding opening bracket, so we return false. If it is not, then we pop the top element off the stack and continue. At the end, if the stack is empty, then all opening brackets have been matched with closing brackets, so we return true. If it is not, then there are unmatched opening brackets, so we return false.
```cpp
#include<stdio.h>
#include<string>
#include<stack>
using namespace std;
bool correct_bracketing(string brackets){
    stack<char> s;
    for(char c : brackets){
        if(c == '<'){
            s.push(c);
        }else if(c == '>'){
            if(s.empty()){
                return false;
            }else{
                s.pop();
            }
        }
    }
    return s.empty();
}
```