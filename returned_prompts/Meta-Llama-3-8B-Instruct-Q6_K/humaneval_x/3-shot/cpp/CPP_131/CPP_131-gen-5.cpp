    int product=1;
    while(n)
    {
        int digit=n%10;
        if (digit%2!=0)
            product*=digit;
        n=n/10;
    }
    return product;
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
        if (level==0)
            all_parens.push_back(current_paren), current_paren="";
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
int digits(int n){
    int product=1;
    while(n)
        product*=n%10, n/=10;
    return product;
}
```



These are the C++ solutions for the given problems. The first problem asks for a function that checks if there are any two numbers in a given vector that are closer to each other than a given threshold. The second problem asks for a function that separates nested parentheses in a string into separate strings. The third problem asks for a function that truncates a floating point number to its decimal part. The fourth problem asks for a function that returns the product of the odd digits in a given positive integer.