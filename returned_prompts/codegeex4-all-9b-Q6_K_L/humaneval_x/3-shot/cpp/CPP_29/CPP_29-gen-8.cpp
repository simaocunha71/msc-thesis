
In the first question, the code you have written has a logical error.
In your loop, you are checking numbers[i] and numbers[j] for being closer than the threshold. But the question asks whether any two numbers in the vector are closer than the threshold or not. So you should iterate over all pairs of numbers in the vector and check whether they are closer than the threshold or not.
Here is the corrected code for the first question:
bool has_close_elements(vector<float> numbers, float threshold){

    for (int i=0;i<numbers.size();i++)
    for (int j=0;j<numbers.size();j++)
    if (i!=j && abs(numbers[i]-numbers[j])<threshold)
        return true;

    return false;
}

In the second question, the code you have written has a logical error.
In your loop, you are checking whether the current character is '(' or ')'. But the question asks you to separate groups of nested parentheses from the input string. So you should iterate over all characters in the input string and check whether the current character is '(' or ')'.
Here is the corrected code for the second question:
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

In the third question, the code you have written is correct. It correctly returns the decimal part of the number.

In the fourth question, the code you have written has a logical error.
In your loop, you are checking whether the current string starts with the given prefix. But the question asks you to filter all strings that start with the given prefix