    vector<string> res;
    string tmp = "";
    int open = 0;

    for (char c : paren_string) {
        if (c == '(') {
            open++;
            tmp += c;
        }
        else if (c == ')') {
            open--;
            tmp += c;
            if (open == 0) {
                res.push_back(tmp);
                tmp = "";
            }
        }
        else if (c != ' ') {
            tmp += c;
        }
    }

    return res;
}

int main(){
    vector<string> res = separate_paren_groups("(  )  (( ))  (( )( ))");
    for (string str : res){
        printf("%s\n", str.c_str());
    }
    return 0;
}
```



## Ruby
