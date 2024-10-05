
Your code looks pretty good, but here are a few things I'd like to see you change:

Include guard: Your header files should have include guards, which look like this:
#ifndef MY_HEADER_H
#define MY_HEADER_H

// your code

#endif

Inconsistent use of semicolons: Your first question has a semicolon at the end of the main function definition, while the other ones don't. I'd recommend sticking to one style or the other.
Don't use using namespace std: It's generally considered bad practice to use this in header files, as it can cause name clashes. It's okay to use it in the implementation files. Instead, you can use the std:: prefix for standard library types.
Use proper indentation: Your first function has proper indentation, but the other ones don't. This can make it difficult to read your code.
Use proper naming conventions: Your function names are camelCase, which is fine, but your variable names are not. In C++, variable names should be snake_case, and function names should be camelCase.
Use auto when possible: Instead of specifying the type of a variable, you can use auto, which will automatically deduce the type for you. This can make your code more readable and easier to maintain.
Use const when possible: If a variable is not going to be modified, you should use the const keyword. This can make your code more readable and easier to maintain.
Use iterators instead of indices: Instead of using indices to access elements of a vector, you can use iterators. This can make your code more readable and easier to maintain.
Use std::abs instead of abs: The abs function is not part of the standard library, so it's better to use std::abs instead.
Use std::vector instead of std::vector: The std:: prefix is missing in your function definition. It should be std::vector instead of std::vector.
Use std::string instead of std::string: The std:: prefix is missing in your function definition. It should be std::string instead of std::string.
Use std::endl instead of \n: The std::endl is a manipulator