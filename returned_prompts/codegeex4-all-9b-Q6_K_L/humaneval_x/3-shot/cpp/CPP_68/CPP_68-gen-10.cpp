
In general, the code is very clear, easy to read, and well written. There are a few small things I'd suggest changing. I'll go through each question.
1. has_close_elements
You have a for loop which is iterating over the vector twice, which can be avoided. You can make use of the fact that if you subtract the smallest element from all the elements and then take the absolute value of those, it will give you the difference between each element. You can then take the minimum of these differences and compare it with the threshold. Also, you can make use of the STL function min_element() to get the smallest element in the vector.
2. separate_paren_groups
This is a good implementation, but you can make use of the STL function find() to search for the closing parenthesis. Also, you can make use of the string function pop_back() to remove the last character from the string.
3. truncate_number
This is a good implementation, but you can make use of the STL function floor() to get the floor value of the number.
4. pluck
This is a good implementation, but you can make use of the STL function find_if() to find the first even number in the vector.
I hope this helps!