    vector<int> result;
    string current_paren;
    int level=0;
    int i;
    for (i=0;i<paren_string.length();i++)
    {
        char chr=paren_string[i];
        if (chr=='(')
        {
            level+=1;
            current_paren+=chr;
        }
        if (chr==')')
        {
            level-=1;
            current_paren+=chr;
            if (level==0){
                result.push_back(level);
                current_paren="";
            }
        }
    }
    return result;
}
```



Here are the answers to the problems:

Q1:
```cpp
bool has_close_elements(vector<float> numbers, float threshold){
    int i, j;
    for (i = 0; i < numbers.size(); i++)
        for (j = i + 1; j < numbers.size(); j++)
            if (abs(numbers[i] - numbers[j]) < threshold)
                return true;
    return false;
}
```

Q2:
```cpp
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    char chr;
    int i;
    for (i = 0; i < paren_string.length(); i++) {
        chr = paren_string[i];
        if (chr == '(') {
            level++;
            current_paren += chr;
        }
        if (chr == ')') {
            level--;
            current_paren += chr;
            if (level == 0) {
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        }
    }
    return all_parens;
}
```

Q3:
```cpp
float truncate_number(float number){
    return number - int(number);
}
```

Q4:
```cpp
vector<int> parse_nested_parens(string paren_string){
    vector<int> result;
    string current_paren;
    int level = 0;
    int i;
    for (i = 0; i < paren_string.length(); i++) {
        char chr = paren_string[i];
        if (chr == '(') {
            level++;
            current_paren += chr;
        }
        if (chr == ')') {
            level--;
            current_paren += chr;
            if (level == 0) {
                result.push_back(level);
                current_paren = "";
            }
        }
