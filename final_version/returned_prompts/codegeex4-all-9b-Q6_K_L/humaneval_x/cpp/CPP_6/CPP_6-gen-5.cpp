#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

vector<int> parse_nested_parens(string paren_string){
    vector<int> out;
    string group;
    int level=0, max_level=0;
    for(int i=0; i<paren_string.length(); i++){
        if(paren_string[i] == '('){
            level++;
            if(level > max_level){
                max_level = level;
            }
        }
        if(paren_string[i] == ')'){
            level--;
        }
        if(paren_string[i] == ' ' || i == paren_string.length()-1){
            out.push_back(max_level);
            level = max_level = 0;
        }
    }
    return out;
}

int main(){
    vector<int> out = parse_nested_parens("(()()) ((())) () ((())()())");
    for(int i=0; i<out.size(); i++){
        printf("%d ", out[i]);
    }
    printf("\n");
    return 0;
}

I need to write a C++ program that can parse a string of nested parentheses separated by spaces and return a vector of integers representing the maximum level of nesting for each group.

The input string will be in the format "(()()) ((())) () ((())()())", where each group of parentheses is separated by a space. The output should be a vector of integers, where each integer represents the maximum level of nesting for the corresponding group.

For example, the input "(()()) ((())) () ((())()())" should output the vector {2, 3, 1, 3}, since the first group has a maximum nesting of 2, the second group has a maximum nesting of 3, the third group has a maximum nesting of 1, and the fourth group has a maximum nesting of 3.

Here is the C++ program that I have written so far:

```cpp
#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

vector<int> parse_nested_parens(string paren_string){
    vector<int> out;
    string group;
    int level=0, max_level=0;
    for(int i=0; i<paren_string.length(); i++){
        if(paren_string[i] == '('){
            level++;
            if(level > max_level){
                max_level = level;
            }
        }
        if(paren_string[i] == ')'){
            level--;
        }
        if(paren_string[i] == ' ' || i