
Your code is a little difficult to read because of the lack of white space.  Try to use it more often.  For example, you should have
if (chr=='(')
{
    level+=1;
    current_paren+=chr;
}

rather than
if (chr=='(')level+=1;current_paren+=chr;

Also, you are using the absolute value function incorrectly.  The first argument should be an integer, but you are passing it a float.  You should use
abs((int)numbers[i]-numbers[j])

instead of
abs(numbers[i]-numbers[j])

Finally, you should put your functions into a namespace, such as
namespace mynamespace {
    // function definitions
}

Then, when you call the functions, you must use the namespace name as a prefix, such as
mynamespace::has_close_elements({1.0, 2.0, 3.0}, 0.5);

That makes it clear what functions you are using, and it prevents name conflicts with other functions.