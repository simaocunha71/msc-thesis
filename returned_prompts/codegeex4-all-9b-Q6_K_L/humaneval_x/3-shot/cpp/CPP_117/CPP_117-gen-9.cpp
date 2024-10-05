
The first question is easy:
You've got to iterate through the vector, and for each pair of numbers, check if they are closer than the threshold. You can do that with nested loops (as you are already doing), and then return true if you find any pair that is close enough. If you get to the end of the loop without finding any pair, return false.
Here is your code with the missing part filled in:
bool has_close_elements(vector<float> numbers, float threshold){
    for (int i=0;i<numbers.size();i++)
    for (int j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<threshold)
        return true;
    return false;
}

The second question requires a bit more thought. You will have to iterate through the string, and keep track of the current level of parentheses. You can do this with a simple integer variable. Each time you see an open parenthesis, you can increment this variable. Each time you see a close parenthesis, you can decrement it. When the variable hits 0, it means you've found a complete group of parentheses. You can then add this group to your vector of strings, and start looking for the next group.
Here is your code with the missing part filled in:
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    for (int i=0;i<paren_string.length();i++){
        chr=paren_string[i];
        if (chr=='('){
            level+=1;
            current_paren+=chr;
        }
        if (chr==')'){
            level-=1;
            current_paren+=chr;
            if (level==0