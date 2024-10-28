    vector<int> res;
    string cur;
    int count = 0;
    for(char c: paren_string){
        if(c == ' ') {
            res.push_back(count);
            count = 0;
        } else {
            count += c == '(' ? 1 : -1;
        }
    }
    res.push_back(count);
    return res;
}

int main(){
    string paren_string = "(()())  (()())  ()  (()()()())";
    vector<int> res = parse_nested_parens(paren_string);
    for(int i: res){
        printf("%d ", i);
    }
    return 0;
}
// 