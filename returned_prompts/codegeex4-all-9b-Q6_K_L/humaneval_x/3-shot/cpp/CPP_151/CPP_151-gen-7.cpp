
Your first function seems fine, but the second function doesn't seem to handle the case when there are multiple sets of parentheses that are not nested but also don't contain each other. For example, the input string "( ( ) ) ( ( ) ) ( ( ) )" would be incorrectly parsed as three separate groups. This is because you're checking whether the level is zero every time you encounter a closing parenthesis, which doesn't take into account the possibility that a closing parenthesis might be closing a group that started earlier in the string.
One way to fix this is to keep track of the level separately for each group of parentheses, and then only consider a closing parenthesis to be closing a group if the level for that group is zero. Here's a modified version of your function that does this:
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    vector<int> levels;
    string current_paren;
    char chr;
    int i;
    for (i=0;i<paren_string.length();i++){
        chr=paren_string[i];
        if (chr=='('){
            levels.push_back(0);
            current_paren+=chr;
        } else if (chr==')'){
            levels.back()++;
            current_paren+=chr;
            if (levels.back()==0){
                all_parens.push_back(current_paren);
                current_paren="";
                levels.pop_back();
            }
        }
    }
    return all_parens;
}

As for the third function, it's not clear what the expected behavior is when the number is negative or not an integer. The current implementation simply returns 0 in these cases, which is fine if that's the desired behavior. However, if you want to handle these cases differently, you'll need to modify the function accordingly.
Finally, the fourth function has a minor issue with the use of the pow function. Since the argument is a float, the result will also be a float, which means that the sum will be a float, not a long long. If you want the sum to be a long long, you'll need to cast the result of pow to a long long before adding