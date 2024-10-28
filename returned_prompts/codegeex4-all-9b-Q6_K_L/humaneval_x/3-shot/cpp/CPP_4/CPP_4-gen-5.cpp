
has_close_elements
Your function has a common mistake, you're comparing i and j but you're comparing the elements of the vector with the index number i and j. You should compare numbers[i] and numbers[j].
bool has_close_elements(vector<float> numbers, float threshold){
    for (int i=0;i<numbers.size();i++)
        for (int j=i+1;j<numbers.size();j++)
            if (abs(numbers[i]-numbers[j])<threshold)
                return true;
    return false;
}

separate_paren_groups
Your function is correct. Just a small optimization can be done to avoid the space complexity. Instead of creating a new string current_paren you can use a stringstream. Here's how you can do it:
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    int level=0;
    char chr;
    stringstream current_paren;
    int i;
    for (i=0;i<paren_string.length();i++)
    {
        chr=paren_string[i];
        if (chr=='(')
        {
            level+=1;
            current_paren<<chr;
        }
        if (chr==')')
        {
            level-=1;
            current_paren<<chr;
            if (level==0){
                all_parens.push_back(current_paren.str());
                current_paren.str("");
            }
        }
    }
    return all_parens;
}

truncate_number
Your function is correct. Just a small optimization can be done. You can use the fmod function to do the modulo operation.
float truncate_number(float number){
    return fmod(number, 1.0);
}

mean_absolute_deviation
Your function is correct. Here's the same function with some minor changes to make it more readable:
float mean_absolute_deviation(vector<float> numbers){
    float mean = 0;
    for (int i=0;i<numbers.size();i++)
        mean += numbers[i];
    mean /= numbers.size();

    float deviation = 0;
    for (int i=0;i<numbers.size();