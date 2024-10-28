    int i;
    string res="";
    for (i=0;i<a.length();i++)
    {
        if ((a[i]-'0')^ (b[i]-'0')) res+=('0'+(a[i]-'0'));
        else res+=('0'+(b[i]-'0'));
    }
    return res;
}
```



**Answers:**

Q1:
```c
bool has_close_elements(vector<float> numbers, float threshold){
    for (int i=0;i<numbers.size();i++)
        for (int j=i+1;j<numbers.size();j++)
            if (abs(numbers[i]-numbers[j])<threshold)
                return true;
    return false;
}
```

Q2:
```c
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
        if (level==0)
            all_parens.push_back(current_paren), current_paren="";
    }
    return all_parens;
}
```

Q3:
```c
float truncate_number(float number){
    return number-float(int(number));
}
```

Q4:
```c
string string_xor(string a,string b){
    string res="";
    for (int i=0;i<a.length();i++)
        res+=(a[i]-'0'^b[i]-'0')+'0';
    return res;
}
```

Note: These solutions are written in C++ and are based on the given problem descriptions and the provided test cases. They may not be the most efficient or optimal solutions, but they should work correctly for the given inputs.