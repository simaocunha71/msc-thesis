
has_close_elements

The code looks okay. But you don't need a label A to break out of the loop. You can simply return false when you find a pair. And you don't need to check the size of the vector for each iteration. You can do that once at the start of the function.
int i, j;
for (i = 0, j = i + 1; j < numbers.size(); i++, j++) {
    if (abs(numbers[i] - numbers[j]) < threshold)
        return true;
}
return false;

separate_paren_groups

The code looks okay but you have a bug. If the input string is like "( ) (( )) (( )( ))", you will get {"()", "(())", "(()())"} but the expected output is {"()", "(())", "(()())", "(( ))"}.
This is because when you encounter a closing brace, you check if the level is 0. But if the input string is like "( ) (( )) (( )( ))", when you encounter the last closing brace, the level is 0, but the group is not complete. So you need to check if the current_paren is not empty before adding it to all_parens.
for (i = 0; i < paren_string.length(); i++) {
    chr = paren_string[i];
    if (chr == '(') {
        level += 1;
        current_paren += chr;
    }
    if (chr == ')') {
        level -= 1;
        current_paren += chr;
        if (level == 0 && current_paren != "") {
            all_parens.push_back(current_paren);
            current_paren = "";
        }
    }
}

truncate_number

The code looks okay but you don't need to use the abs function here. You can simply subtract the integer part from the number.
return number - int(number);

filter_integers

The code looks okay but you can simplify it using a range-based for loop.
vector<int> filter_integers(list_any values) {
    vector<int> int_vec;
    for (auto &value : values) {
        if (value.type