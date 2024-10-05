Here are the solutions for each question:

1. Check if in given vector of numbers, are any two numbers closer to each other than given threshold.

```c++
bool has_close_elements(vector<float> numbers, float threshold){
    for (int i=0;i<numbers.size();i++)
    for (int j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<threshold)
    return true;
    return false;
}
```

2. Separate groups of nested parentheses in a string into separate strings and return them in a vector.

```c++
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    for (int i=0;i<paren_string.length();i++)
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

3. Given a positive floating point number, it can be decomposed into an integer part (largest integer smaller than given number) and decimals (leftover part always smaller than 1). Return the decimal part of the number.

```c++
float truncate_number(float number){
    return number-float(int(number));
}
```

4. Given a non-empty vector of integers lst, add the even elements that are at odd indices.

```c++
int add(vector<int> lst){
    int sum = 0;
    for (int i=0; i<lst.size(); i++)
    {
        if (i%2!=0 && lst[i]%2==0)
        sum+=lst[i];
    }
    return sum;
}
```


These are the solutions for each of the questions. I hope this helps! Let me know if you have any further questions.