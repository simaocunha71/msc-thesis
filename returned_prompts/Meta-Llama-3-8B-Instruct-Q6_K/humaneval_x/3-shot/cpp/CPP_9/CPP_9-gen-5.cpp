    vector<int> max_values;
    int current_max=numbers[0];
    max_values.push_back(current_max);
    for (int i=1;i<numbers.size();i++)
    {
        if (numbers[i]>current_max)
        {
            current_max=numbers[i];
        }
        max_values.push_back(current_max);
    }
    return max_values;
}
```

This is a collection of C++ problems and their solutions. The problems are from various sources, including LeetCode, HackerRank, and other online platforms. The solutions are written in C++ and are intended to be used as a reference for students and developers who are learning C++ or want to improve their skills in the language.

Each problem has a description, input, and expected output. The description explains the problem and its constraints. The input is the data that the program should read from, and the expected output is the result that the program should produce. The solution is a C++ program that solves the problem.

The problems cover a range of topics, including data structures, algorithms, and programming concepts. They are designed to be challenging but not impossible to solve, and they are intended to help students and developers improve their skills in C++.

Here are some examples of the problems and their solutions:

1. Check if in given vector of numbers, are any two numbers closer to each other than given threshold.
```c
bool has_close_elements(vector<float> numbers, float threshold){
    int i,j;
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<threshold)
    return true;
    return false;
}
```

2. Separate groups of nested parentheses in a string.
```c
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

