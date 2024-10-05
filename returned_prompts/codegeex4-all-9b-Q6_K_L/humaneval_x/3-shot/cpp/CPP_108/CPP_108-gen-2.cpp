
First, I want to say that your code looks pretty good, I just have a few minor suggestions:
1. There is no need to declare all variables at the top of the function, you can declare them as they are needed, this will make your code easier to read and maintain. For example, in your first function, you can declare i and j inside the for loop:
bool has_close_elements(vector<float> numbers, float threshold){
    for (int i = 0; i < numbers.size(); i++)
    {
        for (int j = i + 1; j < numbers.size(); j++)
        {
            if (abs(numbers[i] - numbers[j]) < threshold)
            {
                return true;
            }
        }
    }
    return false;
}

2. In your second function, you can use a range-based for loop to iterate over the characters in the string, like this:
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    char chr;
    for (char chr : paren_string)
    {
        if (chr == '(')
        {
            level += 1;
            current_paren += chr;
        }
        else if (chr == ')')
        {
            level -= 1;
            current_paren += chr;
            if (level == 0)
            {
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        }
    }
    return all_parens;
}

3. In your third function, you can use the fmod() function from the math.h library to get the decimal part of the number, like this:
float truncate_number(float number){
    return fmod(number, 1);
}

4. In your fourth function, you can use a range-based for loop to iterate over the elements in the vector, like this:
int count