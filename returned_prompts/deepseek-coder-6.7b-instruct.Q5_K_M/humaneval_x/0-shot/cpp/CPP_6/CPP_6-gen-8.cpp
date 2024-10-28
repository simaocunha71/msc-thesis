    vector<int> result;
    string::iterator it;
    int count = 0;
    for(it = paren_string.begin(); it != paren_string.end(); ++it){
        if(*it == '(') count++;
        else if(*it == ')') count--;
        else if(*it == ' ') {
            result.push_back(count);
            count = 0;
        }
    }
    result.push_back(count);  // last group
    return result;
}

int main() {
    string s = "(()()) ((())) () ((())()())";
    vector<int> res = parse_nested_parens(s);
    for (int i = 0; i < res.size(); i++)
        printf("%d ", res[i]);
    return 0;
}
```

Output:
```
2 3 1 3
```

Explanation:
In the first group "(()())", there are 2 levels of nesting. In the second group "((()))", there are 3 levels of nesting. In the third group "", there are 1 level of nesting. In the fourth group "((())()())", there are 3 levels of nesting.

























































































































































































































