
has_close_elements()
There are a few minor issues with this function:

You can avoid the use of an explicit label by using a break statement to exit the loop.
Instead of using a for loop, you can use the STL algorithms std::min_element and std::max_element to get the minimum and maximum elements of the vector.
You don't need to use abs() to compare floating point numbers. The difference between two floating point numbers is already a floating point number, and will automatically convert to bool when compared to a threshold.

Here's a version of your function that addresses these issues:
bool has_close_elements(vector<float> numbers, float threshold)
{
    auto min_it = std::min_element(numbers.begin(), numbers.end());
    auto max_it = std::max_element(numbers.begin(), numbers.end());

    return *max_it - *min_it < threshold;
}

separate_paren_groups()
There are a few minor issues with this function:

You don't need to use int to loop over a string. You can use a range-based for loop, which will automatically loop over the characters of the string.
You don't need to use a character variable to store the current character. You can directly compare the character to '(' and ')'.
You don't need to use a level variable to track the nesting level of the parentheses. You can simply increment the level when you see an opening parenthesis and decrement it when you see a closing parenthesis.
You don't need to use a separate string variable to build the current parenthesis group. You can directly append the current character to the current_paren string.
You don't need to check for level==0 to push the current_paren string to the all_parens vector. You can simply push the current_paren string to the vector whenever a closing parenthesis is encountered.

Here