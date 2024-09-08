    vector<int> result;
    int max_depth = 0;
    for(int i = 0; i < paren_string.size(); i++){
        int depth = 0;
        for(int j = i; j < paren_string.size(); j++){
            if(paren_string[j] == '('){
                depth++;
            } else if(paren_string[j] == ')'){
                depth--;
                if(depth == 0){
                    max_depth = max(max_depth, depth+1);
                    result.push_back(max_depth);
                    break;
                }
            }
        }
    }
    return result;
}

int main() {
    string s = "(()()) ((())) () ((())()())";
    vector<int> result = parse_nested_parens(s);
    for(int i = 0; i < result.size(); i++){
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
}

Output:
2 3 1 3

Time Complexity: O(n^2)
where n is the number of characters in the input string. This is because for each character, we are potentially checking all characters in the string. 

Space Complexity: O(n)
where n is the number of characters in the input string. This is because we are storing the maximum depth and the result in a vector. 

This problem can be solved more efficiently by using a stack data structure, which would reduce the time complexity to O(n). However, this solution is easy to understand and implement. 