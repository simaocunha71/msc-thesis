
For your first question, here's a more efficient way of doing it.  This version only requires a single pass through the list of numbers.  It uses a boolean variable to remember whether or not a close pair has been found.  If one is found, the function immediately returns true.  If no close pair is found after all numbers have been checked, the function returns false.
bool has_close_elements(vector<float> numbers, float threshold)
{
    bool close_found = false;
    for (unsigned int i = 0; i < numbers.size() - 1 && !close_found; i++)
    {
        for (unsigned int j = i + 1; j < numbers.size() && !close_found; j++)
        {
            if (abs(numbers[i] - numbers[j]) < threshold)
            {
                close_found = true;
            }
        }
    }
    return close_found;
}

For your second question, here is a more efficient version using a single string variable and an index variable.  The string variable is built up character by character as the function scans through the input string.  When an open parenthesis is found, the level is incremented and the character is added to the string variable.  When a close parenthesis is found, the level is decremented.  If the level ever goes to zero, the string variable is added to the vector of strings and then reset.  This version is more efficient than the version you provided because it does not require the construction of a string object for each parenthesis group found.
vector<string> separate_paren_groups(string paren_string)
{
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    char chr;
    int i = 0;
    while (i < paren_string.length())
    {
        chr = paren_string