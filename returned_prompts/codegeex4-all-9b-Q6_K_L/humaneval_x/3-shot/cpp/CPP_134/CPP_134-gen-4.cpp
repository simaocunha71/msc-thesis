
In has_close_elements, you are accessing the vector outside of the bounds.  You should change the range of your loop to start at i+1, not i.
Also, your return type is bool, but you're using int in your return statements.  It should be return true or return false instead of return 1 or return 0.
Here's the corrected version:
bool has_close_elements(vector<float> numbers, float threshold){
    for (int i=0; i<numbers.size(); i++)
        for (int j=i+1; j<numbers.size(); j++)
            if (abs(numbers[i]-numbers[j])<threshold)
                return true;

    return false;
}

In separate_paren_groups, your code is missing the check for spaces.  You should add a condition to skip spaces.
Here's the corrected version:
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    int i;
    for (i=0; i<paren_string.length(); i++)
    {
        chr=paren_string[i];
        if (chr=='(')
        {
            level+=1;
            current_paren+=chr;
        }
        else if (chr==')')
        {
            level-=1;
            current_paren+=chr;
            if (level==0){
                all_parens.push_back(current_paren);
                current_paren="";
            }
        }
        else if (chr!=' ') // Skip spaces
        {
            current_paren+=chr;
        }
    }
    return all_parens;
}

In truncate_number, you should use the fmod function to get the decimal part of the number.
Here's the corrected version:
float truncate_number(float number){
    return fmod(number, 1);
}

In check_if_last_char_is_a_letter, you should check if the last character is a letter before checking if it's a space.  You can use the isalpha function to check if a character is a letter.
Here's the corrected version:
bool check_if_last_char_is_a_letter(string txt){
    int i;
    i = txt.length()-1;
    if (i < 0) // Check if the string is empty