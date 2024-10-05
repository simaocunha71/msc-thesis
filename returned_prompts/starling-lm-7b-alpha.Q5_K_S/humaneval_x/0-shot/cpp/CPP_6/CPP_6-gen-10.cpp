    vector<int> levels;
    for(auto c : paren_string){
        if(c == '('){
            int cur_level = levels.size();
            levels.push_back(cur_level);
        }
        else if(c == ')'){
            levels.pop_back();
        }
    }
    return levels;
}



int main(){
    parse_nested_parens("(()()) ((())) () ((())()())");
}


*/
import re
def parse_nested_parens(paren_string):
    levels = []
    for c in paren_string:
        if c == '(':
            levels.append(len(levels))
        elif c == ')':
            levels.pop()
    return levels

parse_nested_parens("(()()) ((())) () ((())()())")





/*
def parse_nested_parens(paren_string):
    levels = []
    for c in paren_string:
        if c == '(':
            levels.append(len(levels))
        elif c == ')':
            levels.pop()
    return levels

parse_nested_parens("(()()) ((())) () ((())()())")
*/
























































































































































































































