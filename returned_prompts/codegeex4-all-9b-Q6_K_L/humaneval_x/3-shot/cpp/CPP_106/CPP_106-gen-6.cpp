
In C++, we use the std::abs function to get the absolute value of a number. So replace this:
if (abs(numbers[i]-numbers[j])<threshold)
return true;

with this:
if (std::abs(numbers[i]-numbers[j])<threshold)
return true;

In the second problem, you are not checking if the characters are parentheses, only if they are not spaces. You should replace this:
if (chr=='(')

with this:
if (chr=='(' || chr==')')

In the third problem, you are not correctly getting the fractional part of the number. You are trying to subtract the integer part from the number, but you are using the int() cast, which will truncate the number, not convert it to an integer. You should replace this:
return number-int(number);

with this:
return number - static_cast<float>(int(number));