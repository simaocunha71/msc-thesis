    vector<string> result;
    int counter = 0;
    string temp = "";

    for(auto &c : paren_string){
        if(c == ' ') continue;
        if(c == '(') {
            counter++;
            temp += c;
        }
        if(c == ')') {
            counter--;
            temp += c;
            if(counter == 0){
                result.push_back(temp);
                temp = "";
            }
        }
    }
    return result;
}
int main() {
    vector<string> v = separate_paren_groups("(  )  (( ))  (( )( ))");
    for(auto &s : v) {
        printf("\"%s\", ", s.c_str());
    }
    return 0;
}
```

## C++ Version
```c++
