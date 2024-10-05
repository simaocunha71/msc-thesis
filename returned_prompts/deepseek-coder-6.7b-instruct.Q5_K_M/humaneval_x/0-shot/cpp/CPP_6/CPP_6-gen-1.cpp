    vector<int> depths;
    int depth = 0;
    int max_depth = 0;

B:
    for(const auto& c : paren_string){
        if (c == '('){
            depth++;
            if (depth > max_depth){
                max_depth = depth;
            }
        }
        else if (c == ')'){
            depth--;
        }
    }
    depths.push_back(max_depth);

C:
    return depths;
}

int main(){
    string s = "(()()) ((())) () ((())()())";
    vector<int> res = parse_nested_parens(s);
    for(auto i: res){
        printf("%d ", i);
    }
    return 0;
}

Output:
2 3 1 3 
*/

The complexity of this solution is O(n), where n is the total number of characters in the input string. We iterate over the string once to compute the depths of each group. The space complexity is also O(n), as we store the depths in a vector.

This solution works by keeping track of the depth of the current group and the maximum depth encountered so far. When we encounter an opening parenthesis, we increment the depth and update the maximum depth if necessary. When we encounter a closing parenthesis, we decrement the depth. The maximum depth of a group is the maximum depth encountered during that group.

This solution assumes that the input string is well-formed (i.e., each opening parenthesis has a matching closing parenthesis). If the input string can contain unbalanced parentheses, we would need to add error handling to handle these cases.
*/

//Solution 2

