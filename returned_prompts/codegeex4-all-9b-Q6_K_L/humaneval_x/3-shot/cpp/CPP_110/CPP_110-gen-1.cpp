
has_close_elements
The name of the function is not descriptive enough. What is the meaning of "elements"? Are they the values in the vector? Or are they the indices of the vector? You should call it something like has_close_values or has_close_vector_elements.
The variable names are also not descriptive enough. What is the meaning of i and j? Are they indices of the vector? Or are they the elements of the vector? You should call them something like index1 and index2 or value1 and value2.
The function is not well documented. What is the meaning of the threshold parameter? What does the function return? You should add comments to explain these things.
The function is also not well optimized. It is possible to find a pair of close elements in a single pass through the vector, without the need to use nested loops. Here is an example implementation:

bool has_close_elements(vector<float> numbers, float threshold)
{
    for (size_t i = 1; i < numbers.size(); ++i)
    {
        if (abs(numbers[i] - numbers[i-1]) < threshold)
        {
            return true;
        }
    }
    return false;
}

separate_paren_groups
The name of the function is not descriptive enough. What is the meaning of "separate" and "paren" groups? You should call it something like split_paren_groups.
The variable names are also not descriptive enough. What is the meaning of level and current_paren? You should call them something like nesting_level and current_group.
The function is not well documented. What is the meaning of the paren_string parameter? What does the function return? You should add comments to explain these things.
The function is also not well optimized. It is possible to split the groups in a single pass through the string, without the need to use nested loops. Here is an example implementation:

vector<string> separate_paren_groups(const string&