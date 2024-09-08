    vector<int> result;
    int max_depth = 0;
    int current_depth = 0;
    for(int i = 0; i < paren_string.length(); i++){
        if(paren_string[i] == '('){
            current_depth++;
            if(current_depth > max_depth){
                max_depth = current_depth;
            }
        }
        else if(paren_string[i] == ')'){
            current_depth--;
        }
    }
    result.push_back(max_depth);
    return result;
}
int main(int argc, char* argv[])
{
    string input = "(()()) ((())) () ((())()())";
    vector<int> output = parse_nested_parens(input);
    for(int i = 0; i < output.size(); i++)
        printf("%d ", output[i]);
    printf("\n");
    return 0;
}

// Test cases
// parse_nested_parens("(()()) ((())) () ((())()())") {2, 3, 1, 3}
// parse_nested_parens("((()))") {3}
// parse_nested_parens("()") {1}
// parse_nested_parens("()()") {1, 1}
// parse_nested_parens("(()())(()())") {2, 2}
// parse_nested_parens("((()))(()())") {3, 2}
// parse_nested_parens("((()))()(()())") {3, 2} // 3 and 2 are the deepest level of nesting for each group.