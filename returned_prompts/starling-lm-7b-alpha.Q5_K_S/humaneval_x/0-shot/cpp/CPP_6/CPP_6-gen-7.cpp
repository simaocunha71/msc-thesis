vector<int> parse_nested_parens(string paren_string){
    vector<int> ret;
    int max = 0;
    int count = 0;
    for(int i = 0; i < paren_string.size(); i++){
        if(paren_string[i] == '(') count++;
        if(paren_string[i] == ')') count--;
        if(count > max) max = count;
        if(paren_string[i] == '(' && count == max) ret.push_back(max);
    }
    return ret;
}

int main(){
    vector<int> ret = parse_nested_parens("(()()) ((())) () ((())()())");
    for(int i = 0; i < ret.size(); i++) printf("%d ", ret[i]);
    return 0;
}









































































































