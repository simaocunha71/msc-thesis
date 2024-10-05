    vector<int> all_levels;
    int i,level=0;
    for (i=0;i<paren_string.length();i++)
    {
        if (paren_string[i]=='(')
            level+=1;
        if (paren_string[i]==')')
            level-=1;
        all_levels.push_back(level);
    }
    return all_levels;
}  // https://www.geeksforgeeks.org/evaluate-boolean-expression-using-nested-parentheses/
// https://www.geeksforgeeks.org/parse-nested-parentheses-string/
// https://www.geeksforgeeks.org/evaluate-boolean-expression-using-nested-parentheses/
// https://www.geeksforgeeks.org/parse-nested-parentheses-string/
// https://www.geeksforgeeks.org/evaluate-boolean-expression-using-nested-parentheses/
// https://www.geeksforgeeks.org/parse-nested-parentheses-string/
// https://www.geeksforgeeks.org/evaluate-boolean-expression-using-nested-parentheses/
// https://www.geeksforgeeks.org/parse-nested-parentheses-string/
// https://www.geeksforgeeks.org/evaluate-boolean-expression-using-nested-parentheses/
// https://www.geeksforgeeks.org/parse-nested-parentheses-string/
// https://www.geeksforgeeks.org/evaluate-boolean-expression-using-nested-parentheses/
// https://www.geeksforgeeks.org/parse-nested-parentheses-string/
// https://www.geeksforgeeks.org/evaluate-boolean-expression-using-nested-parentheses/
// https://www.geeksforgeeks.org/parse-nested-parentheses-string/
// https://www.geeksforgeeks.org/evaluate-boolean-expression-using-nested-parentheses/
// https://www.geeksforgeeks.org/parse-nested-parentheses-string/
// https://www.geeksforgeeks.org/evaluate-boolean-expression-using-nested-parentheses/
// https://www.geeksforgeeks.org/parse-nested-parentheses-string/
// https://www.geeksforgeeks.org/evaluate-boolean-expression-using-nested-parentheses/
// https://www.geeksforgeeks.org/parse-nested-parentheses-string/
// https://www.geeksforgeeks.org/evaluate-boolean-expression-using-nested-parentheses/
// https://www.geeksforgeeks.org/parse-nested-parentheses-string/
// https://www.geeksforgeeks