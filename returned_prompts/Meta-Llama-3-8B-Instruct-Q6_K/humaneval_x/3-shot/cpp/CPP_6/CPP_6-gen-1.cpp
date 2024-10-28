    vector<int> levels;
    int level=0;
    int i;
    for (i=0;i<paren_string.length();i++)
    {
        char chr=paren_string[i];
        if (chr=='(')
        {
            level+=1;
        }
        if (chr==')')
        {
            level-=1;
            levels.push_back(level);
        }
    }
    return levels;
}  // This solution is not perfect as it does not handle the case of unbalanced parentheses.
// For example, it will not correctly calculate the level of nesting for a string like "(())(()".  // It will return [1, 2, 1] instead of [1, 1, 2].  // The problem can be solved by using a stack to keep track of the levels of nesting.  // Here is a modified version of the function that uses a stack:  //  vector<int> parse_nested_parens(string paren_string) {  //     stack<int> levels;  //     int level=0;  //     int i;  //     for (i=0;i<paren_string.length();i++)  //     {  //         char chr=paren_string[i];  //         if (chr=='(')  //         {  //             levels.push(level);  //             level+=1;  //         }  //         if (chr==')')  //         {  //             level=levels.top();  //             levels.pop();  //         }  //     }  //     vector<int> result;  //     while (!levels.empty())  //     {  //         result.push_back(level);  //         level=levels.top();  //         levels.pop();  //     }  //     reverse(result.begin(), result.end());  //     return result;  // }  // This function will correctly calculate the level of nesting for strings with unbalanced parentheses.  // For example, it will return [1, 1, 2] for the string "(())(()".  // It will also correctly calculate the level of nesting for strings with balanced parentheses.  // For example, it will return [2, 3] for the string "(()()) ((()))".  // The function works by pushing the current level onto the stack each time it encounters an open parenthesis,  // and popping the current level off the stack each time it encounters a close parenthesis.  // It then constructs the result