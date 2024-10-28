    int counter = 0;
    for(char& c : brackets){
        switch(c) {
            case '<':
                counter++;
                break;
            case '>':
                if(counter == 0)
                    return false;
                counter--;
                break;
            default:
                return false;
        }
    }

    return counter == 0;
}

int main(){
    printf("%d\n", correct_bracketing("<"));
    printf("%d\n", correct_bracketing("<>"));
    printf("%d\n", correct_bracketing("<<><>>"));
    printf("%d\n", correct_bracketing("><<>"));
    return 0;
}


A: Your code is almost correct, but the way you are checking the brackets is not optimal. Instead of using a counter, you can use a stack. When you encounter an opening bracket, push it into the stack. When you encounter a closing bracket, pop the top element from the stack. If the stack is empty at the end, return false. If not, return true.

Here is the corrected code:

```cpp
#include<iostream>
#include<stack>
using namespace std;

bool correct_bracketing(string brackets){
    stack<char> s;
    for(char& c : brackets){
        switch(c) {
            case '<':
                s.push(c);
                break;
            case '>':
                if(s.empty())
                    return false;
                s.pop();
                break;
            default:
                return false;
        }
    }

    return s.empty();
}

int main(){
    cout<<correct_bracketing("<")<<endl;
    cout<<correct_bracketing("<>")<<endl;
    cout<<correct_bracketing("<<><>>")<<endl;
    cout<<correct_bracketing("><<>")<<endl;
    return 0;
}
```

This code will return true if every opening bracket has a corresponding closing bracket, and false otherwise.

Note: The `cout`