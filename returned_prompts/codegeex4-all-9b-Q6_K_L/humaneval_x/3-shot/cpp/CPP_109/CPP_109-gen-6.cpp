
First, a warning about the use of C-style headers.  You've included <stdio.h>, but you're not using any of it.  You've included <math.h> for the abs function, but you're not using it either.  You're also using <vector> from the standard C++ library, and <string>, so it's not clear why you're including the C headers at all.  If you're not using them, you should remove them.
The has_close_elements function is almost correct, but has one error: you should be looping from 0 to numbers.size() - 1, not numbers.size() - 2.  The loop should be:
for (i = 0; i < numbers.size() - 1; i++) {
    for (j = i + 1; j < numbers.size(); j++) {
        if (abs(numbers[i] - numbers[j]) < threshold) {
            return true;
        }
    }
}

The separate_paren_groups function is almost correct, but has one error: the code should be:
for (i = 0; i < paren_string.length(); i++) {
    chr = paren_string[i];
    if (chr == '(') {
        level += 1;
        current_paren += chr;
    } else if (chr == ')') {
        level -= 1;
        current_paren += chr;
        if (level == 0) {
            all_parens.push_back(current_paren);
            current_paren = "";
        }
    }
}

The else if is needed to handle the case where chr is a ')', but level is not 0 (i.e., there are unmatched parentheses).
The truncate_number function is correct.
The move_one_ball function is almost correct, but has one error: you should be looping from 0 to arr.size() - 1, not arr.size() - 2.  The loop