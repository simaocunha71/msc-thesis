    vector<int> result;
    int count = 0;
    int max_count = 0;
    for(auto& c : paren_string){
        if(c == '('){
            count++;
            if(count > max_count)
                max_count = count;
        }
        else if(c == ')'){
            count--;
        }
    }
    result.push_back(max_count);
    return result;
}

int main(){
    auto res = parse_nested_parens("(()()) ((())) () ((())()())");
    for(auto r : res)
        printf("%d ", r);
    return 0;
}
*/


A: 
Here is the C++ solution using stack:

```C++
#include <iostream>
#include <string>
#include <stack>
#include <vector>

std::vector<int> parse_nested_parens(std::string paren_string){
    std::vector<int> results;
    std::stack<char> stk;
    int max_depth = 0;
    int curr_depth = 0;
    for(char c : paren_string){
        if(c == '('){
            stk.push(c);
            curr_depth++;
            if(curr_depth > max_depth)
                max_depth = curr_depth;
        }
        else if(c == ')'){
            if(!stk.empty() && stk.top() == '('){
                stk.pop();
                curr_depth--;
            }
        }
        else if(c == ' '){
            results.push_back(max_depth);
            max_depth = 0;
            curr_depth = 0;
        }
    }
    results.push_back(max_depth);
    return results;
}

int main(){
    auto res = parse_nested_parens("(()()) ((())) () ((())()())");
    for(auto r : res)
        std::cout << r << " ";
    return 0;