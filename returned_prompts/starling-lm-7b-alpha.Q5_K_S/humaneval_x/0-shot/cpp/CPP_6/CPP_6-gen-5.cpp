    vector<int> max_nesting;
    int cur_nesting = 0;
    int start = 0;
    while(start < paren_string.length()){
        if(paren_string[start] == '('){
            cur_nesting++;
        }else if(paren_string[start] == ')'){
            cur_nesting--;
        }
        if(start+1 == paren_string.length()){
            max_nesting.push_back(cur_nesting);
            goto B;
        }
        if(paren_string[start+1] == ')'){
            max_nesting.push_back(cur_nesting);
            goto B;
        }
        start++;
    }
    max_nesting.push_back(cur_nesting);

B:;
    return max_nesting;
}

int main(){
    printf("%s\n", parse_nested_parens("(()()) ((())) () ((())()())").empty() ? "True" : "False");
}

*/
import re
def parse_nested_parens(paren_string):
    max_nesting = []
    cur_nesting = 0
    start = 0
    while start < len(paren_string):
        if paren_string[start] == '(':
            cur_nesting += 1
        elif paren_string[start] == ')':
            cur_nesting -= 1

        if start + 1 == len(paren_string):
            max_nesting.append(cur_nesting)
            break
        if paren_string[start + 1] == ')':
            max_nesting.append(cur_nesting)
            break
        start += 1
    max_nesting.append(cur_nesting)
    return max_nesting

def test_parse_nested_parens():
    assert parse_nested_parens("(()()) ((())) () ((())()())") == [2, 3, 1, 3]
    print("All