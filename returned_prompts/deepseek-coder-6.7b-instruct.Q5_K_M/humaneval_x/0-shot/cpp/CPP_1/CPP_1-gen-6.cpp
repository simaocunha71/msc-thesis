
1. Initialize a result vector to store the separate groups.
2. Initialize a stack to keep track of the parentheses.
3. Initialize an empty string to store the current group.
4. Loop over the input string:
    4.1 If the character is an open parenthesis, push it into the stack and append it to the current group.
    4.2 If the character is a close parenthesis, remove one item from the stack and append it to the current group. After appending, if the stack is empty, that means the current group is finished, so push the current group into the result vector and start a new one.
5. Return the result vector.

*/
#include<stack>
vector<string> separate_paren_groups(string paren_string){
    vector<string> result;
    stack<char> s;
    string group = "";
    for(int i=0; i<paren_string.size(); i++){
        if(paren_string[i] == '('){
            s.push(paren_string[i]);
            group += paren_string[i];
        }else if(paren_string[i] == ')'){
            s.pop();
            group += paren_string[i];
            if(s.empty()){
                result.push_back(group);
                group = "";
            }
        }
    }
    return result;
}
```

## [Question 3](https://github.com/srikanth-krishna/InterviewQuestions/blob/master/Programming/C%2B%2B/questions/3.md)

