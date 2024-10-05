
There is a good chance your code is failing because you have not included the correct header for std::abs.  You should use #include <cstdlib> instead of #include <math.h>.  If you are using C++11 or later, you can use #include <cmath> as well.
Also, there is a good chance your code is failing because you have not included the correct header for std::vector.  You should use #include <vector> instead of #include <vector.h>.
On a similar note, you should use the standard library algorithms to perform the sorting and reversing.  This is both more efficient and more readable.  You can replace your loops with the following:
std::sort(numbers.begin(), numbers.end());
std::reverse(numbers.begin(), numbers.end());

Your second function, separate_paren_groups, has a logic error.  You are not correctly checking for the closing of a group.  You should check for a closing parenthesis immediately after you increment the level.  You should also check for the closing parenthesis in the case where level is zero.  Here is the corrected code:
for (i=0;i<paren_string.length();i++)
{
    chr=paren_string[i];
    if (chr=='(')
    {
        level+=1;
        current_paren+=chr;
    }
    else if (chr==')' && level==0)
    {
        all_parens.push_back(current_paren);
        current_paren="";
    }
    else if (chr==')')
    {
        level-=1;
        current_paren+=chr;
    }
}

Your third function, truncate_number, has a bug.  You are casting the float to an int, but this does not truncate the decimal part of the number.  You should use std::floor to truncate the number.
return number - std::floor(number);

Your fourth function, by_length, has a bug.