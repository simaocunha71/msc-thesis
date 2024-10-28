    int n = str.size();
    int open = 0, close = 0;
    for(int i = 0; i < n; i++){
        if(str[i] == '['){
            open++;
        }
        else{
            close++;
        }
        if(close > open){
            return false;
        }
    }
    if(open == close && open > 0){
        return true;
    }
    return false;
}
int main(){
    string s1 = "[[]]", s2 = "[]]]]]]][[[[[]", s3 = "[][]", s4 = "[]", s5 = "[[][]]", s6 = "[[]][[";
    printf("%d\n", is_nested(s1));
    printf("%d\n", is_nested(s2));
    printf("%d\n", is_nested(s3));
    printf("%d\n", is_nested(s4));
    printf("%d\n", is_nested(s5));
    printf("%d\n", is_nested(s6));
    return 0;
}

The function checks for the number of open and closed square brackets in the string. If the number of closed brackets is greater than the number of open brackets, it means there is a closing bracket without a corresponding opening bracket, so the function returns false. The function also returns false if the number of open and closed brackets are equal and greater than 0, because then there are no nested brackets. Otherwise, it returns true.
*/

#include <iostream>
#include <stack>
#include <string>

bool is_nested(std::string str) {
    std::stack<char> stk;

    for (char c : str) {
        if (c == '[') {
            stk.push(c);
        } else {
            if (stk.empty()) {
                return false;
            }
            if (stk.top() == '[') {
                stk.pop();
            } else {
                while (!stk.empty() && stk.top() !=