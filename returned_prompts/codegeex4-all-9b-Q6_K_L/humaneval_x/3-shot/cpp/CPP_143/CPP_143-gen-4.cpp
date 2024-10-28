
has_close_elements

The name of the function should be a verb or a verb phrase. The name you used is a noun phrase.
You also have a redundant comment. The function name already explains what the function does.
You have a redundant variable i. You could use the range-based for loop to iterate over the vector:
for (float num : numbers) {
    for (float other_num : numbers) {
        if (other_num != num && abs(other_num - num) < threshold) {
            return true;
        }
    }
}
return false;

separate_paren_groups

The name of the function should be a verb or a verb phrase. The name you used is a noun phrase.
You have a redundant comment. The function name already explains what the function does.
You have a redundant variable i. You could use the range-based for loop to iterate over the string:
for (char chr : paren_string) {
    if (chr == '(') {
        level++;
        current_paren += chr;
    } else if (chr == ')') {
        level--;
        current_paren += chr;
        if (level == 0) {
            all_parens.push_back(current_paren);
            current_paren = "";
        }
    }
}

truncate_number

The name of the function should be a verb or a verb phrase. The name you used is a noun phrase.
You have a redundant comment. The function name already explains what the function does.

words_in_sentence

The name of the function should be a verb or a verb phrase. The name you used is a noun phrase.
You have a redundant comment. The function name already explains what the function does.
You have a redundant variable i. You could use the range-based for loop to iterate over the string:
