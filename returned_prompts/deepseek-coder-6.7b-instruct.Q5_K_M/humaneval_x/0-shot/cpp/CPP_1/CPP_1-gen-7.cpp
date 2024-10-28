    vector<string> groups;
    string temp = "";
    int count = 0;
    for(char c : paren_string){
        if(c == ' ') continue;
        if(c == '(') {
            count++;
            temp += c;
        }
        if(c == ')') {
            count--;
            temp += c;
            if(count == 0){
                groups.push_back(temp);
                temp = "";
            }
        }
    }
    return groups;
}

*/

#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> separate_paren_groups(string paren_string){

    vector<string> groups;
    string temp = "";
    int count = 0;
    for(char c : paren_string){
        if(c == ' ') continue;
        if(c == '(') {
            count++;
            temp += c;
        }
        if(c == ')') {
            count--;
            temp += c;
            if(count == 0){
                groups.push_back(temp);
                temp = "";
            }
        }
    }
    return groups;
}

int main()
{
    string s = "(  )  (( ))  (( )( ))";
    vector<string> groups = separate_paren_groups(s);
    for(string group : groups){
        cout << group << endl;
    }
    return 0;
}
```

Here, we use a simple approach to solve the problem. We loop through the input string and keep track of the parentheses. When we encounter a closed parenthesis, we check if the count is zero, if it is, then we know that we have found a complete group. We then store that group in our vector and reset the temp string for the next group.

This solution works by ignoring spaces in the input string and also by correctly handling nested parentheses. The time complexity of this solution is O(n), where n is the length of the input string.
*/

// 100%