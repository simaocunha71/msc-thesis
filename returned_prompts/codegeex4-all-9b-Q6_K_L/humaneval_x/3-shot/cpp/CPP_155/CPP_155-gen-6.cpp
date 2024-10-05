
The first function looks correct. There's nothing wrong with the logic or the implementation.
The second function has a potential error. If you input a string with no parentheses, you will get an error. You should add a check at the beginning of the function to see if there are any parentheses in the string. If there are none, return an empty vector.
Here's the corrected function:
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    int i;
    int count=0;
    for (i=0;i<paren_string.length();i++)
    {
        chr=paren_string[i];
        if (chr=='('){
            count+=1;
        }
    }
    if (count==0){
        return all_parens;
    }
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

The third function looks correct. There's nothing wrong with the logic or the implementation.
The fourth function has a potential error. If you input a negative number, the function will return a negative number. You should add an absolute value function to the code so that the function will always return a positive number. Here's the corrected function:
vector<int> even_odd_count(int num){
    vector<int> all_count;
    int n = abs(num);
    int even=0,odd=0;
    while (n>0)
    {
        if (n%2==0) even+=1;
        else odd+=1;
        n=n/10;
    }
    all_count.push_back(even);
   