
has_close_elements
Your loop is correct, but you have a bug in your if statement. It should be:
if (abs(numbers[i]-numbers[j])<threshold) {
    return true;
}

You have a missing brace.

separate_paren_groups
Your code is mostly correct, but it is not handling the case where the input string is empty, which would cause an out-of-bounds error. You should add a check at the beginning of your function to see if the input string is empty and return an empty vector in that case.

truncate_number
Your code is correct, but you should add a check to see if the input number is negative. If it is, you should return 0.0.

sorted_list_sum
Your code is mostly correct, but you have a bug in your if statement. It should be:
if (lst[i].length()%2!=0) {
    lst.erase(lst.begin()+i);
}

You have a missing brace.
Also, you should add a check at the beginning of your function to see if the input vector is empty and return an empty vector in that case.