
You should use std::abs for absolute value, as it is the standard library function for that purpose.  I assume you are using C++11, because std::abs was introduced in C++11.  If not, you can use fabsf or fabs for floats.
You are also using a very verbose for-loop syntax.  C++ has a more concise syntax for for-loops.  You can use this one instead:
for (int i = 0; i < numbers.size(); ++i)

You also have a redundant break statement in your inner loop.  You should remove it.
The same applies to your separate_paren_groups function.  You should use the more concise for-loop syntax instead of the verbose one.  Also, the variable names level and chr are not very descriptive.  You should choose more descriptive names.
You should also use the more concise if syntax.  You can use this one instead:
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

You are also using a very verbose if syntax.  You can use this one instead:
if (chr == '(') {
    ++level;
    current_paren += chr;
} else if (chr == ')') {
    --level;
    current_paren += chr;
    if (level == 0) {
        all_parens.push_back(current_paren);
        current_paren = "";
    }
}

You should also use the more concise return syntax.  You can use this one instead:
return number - static_cast<int>(number);

The same applies to your truncate_number function.  You should use the more concise if syntax instead of the verbose one.  Also, you should use the more concise return syntax instead of the verbose one.
You should also use the more concise