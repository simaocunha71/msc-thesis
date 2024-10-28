
1.
You are comparing a character with a float. This will not work. Change your comparison to:
if (abs(numbers[i]-numbers[j])<threshold)

2.
You are using a for loop to iterate over the string. Use a range based for loop instead:
for (auto chr : paren_string)

3.
You are using int for the number of digits. Use size_t instead. This will prevent potential overflow.
4.
You are using the math library for the abs function. You can use the standard library instead. This will make your code more portable:
if (std::abs(numbers[i]-numbers[j])<threshold)

5.
You are using the math library for the int function. You can use the standard library instead. This will make your code more portable:
return number-int(number);

6.
You are using the math library for the floor function. You can use the standard library instead. This will make your code more portable:
return number-floor(number);

7.
You are using the math library for the ceil function. You can use the standard library instead. This will make your code more portable:
return ceil(number)-number;

8.
You are using the math library for the floor function. You can use the standard library instead. This will make your code more portable:
return floor(number);

9.
You are using the math library for the ceil function. You can use the standard library instead. This will make your code more portable:
return ceil(number);

10.
You are using the math library for the floor function. You can use the standard library instead. This will make your code more portable:
return floor(number);

11.
You are using the math library for the ceil function. You can use the standard library instead. This will make your code