    vector<int> result;
    while (!lst.empty()){
        int min_val = *min_element(lst.begin(), lst.end());
        result.push_back(min_val);
        lst.erase(remove(lst.begin(), lst.end(), min_val), lst.end());
        if (!lst.empty()){
            int max_val = *max_element(lst.begin(), lst.end());
            result.push_back(max_val);
            lst.erase(remove(lst.begin(), lst.end(), max_val), lst.end());
        }
    }
    return result;
}
```



Here are the answers:

Q1:
```
bool has_close_elements(vector<float> numbers, float threshold){
    for (int i=0;i<numbers.size();i++)
        for (int j=i+1;j<numbers.size();j++)
            if (abs(numbers[i]-numbers[j])<threshold)
                return true;
    return false;
}
```

Q2:
```
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    for (int i=0;i<paren_string.length();i++){
        chr=paren_string[i];
        if (chr=='(')
            level+=1, current_paren+=chr;
        if (chr==')')
            level-=1, current_paren+=chr;
        if (level==0){
            all_parens.push_back(current_paren);
            current_paren="";
        }
    }
    return all_parens;
}
```

Q3:
```
float truncate_number(float number){
    return number-int(number);
}
```

Q4:
```
vector<int> strange_sort_list(vector<int> lst){
    vector<int> result;
    while (!lst.empty()){
        int min_val = *min_element(lst.begin(), lst.end());
        result.push_back(min_val);
        lst.erase(remove(lst.begin(), lst.end(), min_val), lst.end());
        if (!lst.empty()){
            int max_val = *max_element(lst.begin(), lst.end());
            result.push_back(max_val);
            lst.erase(remove(lst.begin(), lst.end(), max_val), lst.end());
        }
    }
    return result;
}
```



I hope this helps! Let me know if you have any further questions.