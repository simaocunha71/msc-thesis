    int count = 0;
    for(char& c : brackets){
        if(c == '('){
            count++;
        }
        else if(c == ')'){
            if(count == 0){
                return false;
            }
            count--;
        }
    }
    return count == 0;
}
int main()
{
    printf("%d",correct_bracketing("(()()()()())"));
    return 0;
}


A: The solution you are looking for is a stack-based solution. You need to iterate through the string and push every opening bracket into a stack, and when you encounter a closing bracket, you check if there is an opening bracket in the stack. If there is, you pop it from the stack. If there isn't, you return false. After going through the whole string, if the stack is empty, you return true. Otherwise, return false.
Here is the code for the problem:

#include<bits/stdc++.h>
using namespace std;

bool correct_bracketing(string brackets) {
    stack<char> s;
    for(char c : brackets) {
        if(c == '(') {
            s.push(c);
        } else if(c == ')') {
            if(s.empty()) {
                return false;
            }
            s.pop();
        }
    }
    return s.empty();
}

int main() {
    cout << (correct_bracketing("(()())") ? "true" : "false") << endl;
    cout << (correct_bracketing(")(()") ? "true" : "false") << endl;
    return 0;
}

In the code, we use a stack of characters to keep track of the opening brackets. When we encounter a closing bracket, we check if there is an opening bracket in the stack. If there is, we pop it from the stack. If there isn't, we return false, because this means there is no matching closing bracket for an opening bracket. After going through the whole string, if the stack is empty, we return true, because all opening brackets have their matching