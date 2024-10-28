
has_close_elements

There's an off-by-one error in your for loops.  They should start at i=1, not i=0.
for (i=1;i<numbers.size();i++)
for (j=i+1;j<numbers.size();j++)

separate_paren_groups

Your function doesn't handle strings with unmatched parentheses.  You'll need to add a check to see if level is zero at the end of the loop.
for (i=0;i<paren_string.length();i++)
{
    chr=paren_string[i];
    if (chr=='(')
    {
    level+=1;
    current_paren+=chr;
    }
    if (chr==')')
    {
        level-=1;
        current_paren+=chr;
        if (level==0){
            all_parens.push_back(current_paren);
            current_paren="";
        }
    }
}
if (level != 0) {
    // Handle unmatched parentheses
}

truncate_number

This function is correct, but it's a bit confusing.  The name "truncate_number" suggests that it will return the integer part of the number, but it actually returns the fractional part.  A more descriptive name would be something like "get_fractional_part".

simplify

This function is not correct.  It only checks if the greatest common divisor of the numerator and denominator is a divisor of both numbers.  This does not guarantee that the result is a whole number.  For example, simplify("1/5", "5/1") will return true, but 1/5 * 5/1 = 1/1, which is a whole number.  To fix this, you need to check if the numerator and denominator are both divisible by the gcd.