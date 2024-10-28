
Your first function is correct. It is not necessary to use a named label for looping. You can use the range-based for loop. That would make your code more readable.
for (auto& num : numbers) {
    for (auto& other : numbers) {
        if (other != num && abs(other - num) < threshold)
            return true;
    }
}
return false;

Your second function is correct. You can use the standard library function string::find to find the next occurrence of the character ')'. This would make your code more readable.
for (size_t i = 0; i < paren_string.length(); ++i) {
    if (paren_string[i] == '(') {
        level += 1;
        current_paren += paren_string[i];
    } else if (paren_string[i] == ')' && --level == 0) {
        current_paren += paren_string[i];
        all_parens.push_back(current_paren);
        current_paren.clear();
    }
}

The third function has a bug. The expression number - int(number) does not truncate the number. It converts the fractional part to an integer. You can use the modulus operator to get the fractional part of the number.
return number - floor(number);

Your fourth function is correct. You can use the standard library function string::compare to compare strings. That would make your code more readable.
for (size_t i = 0; i < operato.size(); ++i) {
    switch (operato[i].compare("+")) {
        case 0: result += operand[i + 1]; break;
        case -1: result -= operand[i + 1]; break;
        case 1: result *= operand[i + 1]; break;
        case 2: result = pow