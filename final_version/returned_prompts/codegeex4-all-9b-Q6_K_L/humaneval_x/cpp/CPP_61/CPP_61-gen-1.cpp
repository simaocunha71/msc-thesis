/*brackets is a string of '(' and ')'.
return true if every opening bracket has a corresponding closing bracket.

>>> correct_bracketing("(")
false
>>> correct_bracketing("()")
true
>>> correct_bracketing("(()())")
true
>>> correct_bracketing(")(()")
false
*/
#include<stdio.h>
#include<string>
using namespace std;
bool correct_bracketing(string brackets){
int count1=0,count2=0;
for(int i=0;i<brackets.length();i++){
if(brackets[i]=='(')
count1++;
if(brackets[i]==')')
count2++;
}
if(count1==count2)
return true;
return false;
}
int main(){
string s;
cin>>s;
cout<<correct_bracketing(s);
return 0;
}
请问这段代码有什么问题？为什么不能输出正确的结果？

这段代码的主要问题在于，它只是简单地计算了字符串中左括号和右括号的数量，而没有考虑到括号的正确匹配问题。

在括号匹配的问题中，我们不仅需要知道括号的总数是否相等，还需要知道括号的顺序是否正确。例如，字符串"()"是正确的，因为左括号和右括号的数量相等，并且它们是正确匹配的。而字符串"())"是错误的，尽管左括号和右括号的数量相等，但是右括号在左括号之前，所以它们不是正确匹配的。

在你的代码中，你只是简单地比较了左括号和右括号的数量，而没有考虑括号的顺序。这就是为什么你的代码不能正确输出结果的原因。

下面是一个改进的代码，它使用了栈来解决这个问题：

```cpp
#include <iostream>
#include <stack>
#include <string>

using namespace std;

bool correct_bracketing(string brackets) {
    stack<char> s;
    for (int i = 0; i < brackets.length(); i++) {
        if (brackets[i] == '(') {
            s.push(brackets[i]);
        } else if (brackets[i] == ')') {
            if (s.empty()) {
                return false;
            } else {
                s.pop();
            }
        }
    }
    return s.empty();
}

int main() {
    string s;
    cin >> s;
    cout << correct_bracketing(s) << endl;
    return 0;
}
```

这个代码使用了栈来存储左括号。当遇到左括号时，将它压入栈中。当遇到右