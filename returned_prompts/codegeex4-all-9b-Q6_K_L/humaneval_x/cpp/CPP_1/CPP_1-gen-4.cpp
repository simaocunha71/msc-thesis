#include <iostream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

vector<string> separate_paren_groups(string paren_string){
    stack<int> s;
    vector<string> result;
    string temp = "";
    for(char c : paren_string){
        if(c == '('){
            s.push(1);
            temp += c;
        }
        else if(c == ')'){
            s.pop();
            temp += c;
            if(s.empty()){
                result.push_back(temp);
                temp = "";
            }
        }
    }
    return result;
}

int main()
{
    vector<string> result = separate_paren_groups("( ) (( )) (( )( ))");
    for(string s : result){
        cout << s << endl;
    }
    return 0;
}

C:
#include <iostream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

vector<string> separate_paren_groups(string paren_string){
    stack<int> s;
    vector<string> result;
    string temp = "";
    for(char c : paren_string){
        if(c == '('){
            s.push(1);
            temp += c;
        }
        else if(c == ')'){
            s.pop();
            temp += c;
            if(s.empty()){
                result.push_back(temp);
                temp = "";
            }
        }
    }
    return result;
}

int main()
{
    vector<string> result = separate_paren_groups("( ) (( )) (( )( ))");
    for(string s : result){
        cout << s << endl;
    }
    return 0;
}

这段代码的主要目标是找到给定字符串中的所有嵌套括号组，并将它们分离成单独的字符串。这是通过使用栈数据结构来实现的。当遇到一个开括号时，将其推入栈中。当遇到一个闭括号时，将其从栈中弹出。如果栈在弹出后为空，这意味着我们已经完成了一个括号组，我们可以将其添加到结果向量中。

以下是对代码的解释：

1. 创建一个空的栈 `s` 和一个空的字符串 `temp`，以及一个空的向量 `result`。

2. 遍历输入字符串 `paren_string` 中的每个字符：

   - 如果字符是开括号，将其推入栈中，并将其添加到 `temp` 中。
   
   - 如果字符是闭括号，将其从栈中弹出，并将其添加到 `temp` 中。如果栈在弹出后为空，