    vector<int> result;
    int depth = 0;
    for(char c : paren_string){
        if(c == '('){
            depth++;
        }
        else if(c == ')'){
            depth--;
        }
        if(result.size() == 0 || result.back() < depth) result.push_back(depth);
    }
    return result;
}



/*
Given a string of parentheses, return a string consisting of all the characters of the input string in the order they appear, but with all the '(' characters coming before all the ')' characters.
E.g. for the string "(()())", the result should be "()()()".

>>> sort_parens("(()())")
"()()()"
*/

string sort_parens(string paren_string){
    vector<char> result;
    for(char c : paren_string){
        if(c == '(' || c == ')'){
            result.push_back(c);
        }
        else{
            result.push_back(c);
        }
    }
    sort(result.begin(), result.end());
    return string(result.begin(), result.end());
}




/*
Given a string of parentheses, return a string consisting of all the characters of the input string in the order they appear, but with all the ')' characters coming before all the '(' characters.
E.g. for the string "(()())", the result should be "())()".

>>> sort_parens_rev("(()())")
"())()"
*/
string sort_parens_rev(string paren_string){
    vector<char> result;
    for(char c : paren_string){
        if(c == '(' || c == ')'){
            result.push_back(c);
        }
        else{
            result.push_back(c);
        }
    }
    sort(result.rbegin(), result.rend());
    return string(result.begin(), result.end());
}





/*
Given a string of parentheses, return a string