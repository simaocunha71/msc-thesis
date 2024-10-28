
Your first function has_close_elements is very close to being correct, but there is one problem:

for (j=i+1;j<numbers.size();j++)

The j loop should start at i+1, because you're already comparing i with all previous elements, so there's no need to do it again. The corrected code:
for (j=i+1;j<numbers.size();j++)

Your second function, separate_paren_groups, is also very close to being correct, but there is a problem with the way you're checking for a level of 0. This will only happen if you encounter a closing parenthesis while the level is 1. If you encounter a closing parenthesis while the level is 0, this will cause an out-of-bounds error. The corrected code:
if (level==0) {
    all_parens.push_back(current_paren);
    current_paren="";
}

Your third function, truncate_number, is correct.

Your fourth function, below_zero, is correct.