/*
You are given a vector of two strings, both strings consist of open
parentheses '(' or close parentheses ')' only.
Your job is to check if it is possible to concatenate the two strings in
some order, that the resulting string will be good.
A string S is considered to be good if and only if all parentheses in S
are balanced. For example: the string "(())()" is good, while the string
"())" is not.
Return "Yes" if there's a way to make a good string, and return "No" otherwise.

Examples:
match_parens({"()(", ")"}) == "Yes"
match_parens({")", ")"}) == "No"
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<stack>
using namespace std;
string match_parens(vector<string> lst){
    int a=0;
    int b=0;
    for(int i=0;i<lst[0].length();i++)
    {
        if(lst[0][i]=='(')
        {
            a++;
        }
        else
        {
            a--;
        }
    }
    for(int i=0;i<lst[1].length();i++)
    {
        if(lst[1][i]=='(')
        {
            b++;
        }
        else
        {
            b--;
        }
    }
    if(a==0&&b==0)
    {
        return "Yes";
    }
    else
    {
        return "No";
    }
}
我想用栈来实现

当然，我们可以利用栈来判断括号是否匹配。对于每个字符，如果它是左括号，我们将其推入栈中。如果它是右括号，我们需要检查栈顶元素是否为对应的左括号，如果是，则将其弹出栈，否则括号不匹配。

下面是使用栈实现的代码：

```cpp
#include <stack>
#include <string>
#include <vector>

using namespace std;

string match_parens(vector<string> lst) {
    stack<char> s;
    string combined = lst[0] + lst[1];
    for (char c : combined) {
        if (c == '(') {
            s.push(c);
        } else if (c == ')') {
            if (s.empty() || s.top() != '(') {
                return "No";
            }
            s.pop();
        }
    }
    return s.empty() ? "Yes" : "No";
}
```

这个函数首先