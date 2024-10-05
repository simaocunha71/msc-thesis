    for(int i = 0; i < lst1.size(); i++) {
        bool found = false;
        for(int j = 0; j < lst2.size(); j++) {
            if(lst1[i] % 2 != 0 && lst2[j] % 2 == 0) {
                swap(lst1[i], lst2[j]);
                found = true;
                break;
            }
        }
        if(!found) {
            return "NO";
        }
    }
    return "YES";
}
```



## 1. has_close_elements

The function `has_close_elements` takes a vector of floating point numbers and a threshold as input. It checks if there are any two numbers in the vector that are closer to each other than the given threshold. If it finds such a pair, it returns `true`; otherwise, it returns `false`.

Here is the implementation:

```c++
bool has_close_elements(vector<float> numbers, float threshold){
    int i, j;
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<threshold)
    return true;

    return false;
}
```

## 2. separate_paren_groups

The function `separate_paren_groups` takes a string containing nested parentheses as input. It separates the groups of parentheses into separate strings and returns a vector of those. The groups are balanced and not nested within each other. Ignoring any spaces in the input string.

Here is the implementation:

```c++
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    int i;
    for (i=0;i<paren_string.length();i++)
    {
        chr=paren_string[i];
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
                all_parens.push_back(current_paren);
                current_paren="";
            }
        }
    }
    return all_parens;
}
```

## 3. truncate_number

The function `truncate_number` takes a floating point number as input. It returns the decimal part of the number.

Here is the implementation:

```c++
float