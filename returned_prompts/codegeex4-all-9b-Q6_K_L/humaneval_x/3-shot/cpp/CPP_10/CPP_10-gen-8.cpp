
For the first question, you have a bug in your code. You return true as soon as you find two numbers closer than your threshold, but what if the next numbers are not close enough? You should iterate through all pairs of numbers and only return true if you've checked all of them and found no two close enough. Your code would look like this:
bool has_close_elements(vector<float> numbers, float threshold){
    for (int i=0;i<numbers.size();i++)
        for (int j=i+1;j<numbers.size();j++)
            if (abs(numbers[i]-numbers[j])<threshold)
                return true;
    return false;
}

For the second question, you have another bug. You don't actually check if the parentheses are balanced. You just check if the level is 0, which will only be true when you've seen an equal number of open and close parentheses, but not necessarily when they're balanced. You should check if the level is ever negative, which would indicate an unbalanced string.
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    int i;
    for (i=0;i<paren_string.length();i++){
        chr=paren_string[i];
        if (chr=='('){
            level+=1;
            current_paren+=chr;
        }
        if (chr==')'){
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

For the third question, you have a bug in your code. You're using the floor function to truncate the number, but you should be using the fmod function instead. The fmod function gives you the remainder of a division operation, which is what you want for truncating a number.
float truncate_number(float number){
    return fmod(number, 1);
}

For the fourth question, your code is correct. You're reversing the string and comparing it to the original, which is the correct way to check if a string is a palindrome.
bool is_palindrome(string str){
    string s(str.rbegin(),str.rend());
    return s==str;
}

For the fifth question, you have a bug