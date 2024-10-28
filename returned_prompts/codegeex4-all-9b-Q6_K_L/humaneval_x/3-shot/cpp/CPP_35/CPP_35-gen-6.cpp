
Here are some general comments:

Avoid using namespace std;
It's not good practice to use it in header files, but it's okay in implementation files.
Avoid using C library functions when the C++ Standard Library has a better alternative. For example, use the std::abs function instead of the C abs function, and use std::pow instead of pow.
Avoid using the preprocessor to define macros. They're hard to debug and they're not portable to non-C languages. Use inline functions or constexpr functions instead.
Avoid using magic numbers. They're hard to understand and they're easy to change accidentally. For example, in your code, you use the number 0.3. This number isn't self-explanatory and it's not clear what it means. It would be better to define a constant with a meaningful name, such as const float threshold = 0.3f;
Avoid using single-character variable names. They're hard to understand and they're easy to change accidentally. For example, in your code, you use the variable names i and j. These variable names aren't self-explanatory and it's not clear what they represent. It would be better to define variables with meaningful names, such as forLoopIndex and innerLoopIndex.
Avoid using the goto statement. It's not good practice to use it in modern C++ programming. It's hard to understand and it's easy to change accidentally. For example, in your code, you use the goto statement to jump from the end of the for loop to the end of the function. It would be better to use a return statement instead.
Avoid using the A: label. It's not good practice to use it in modern C++ programming. It's hard to understand and it's easy to change accidentally. For example, in your code, you use the label A: to jump from the end of the for loop to the end of the function. It would be better to use a return statement instead.
Avoid using the A: label. It's not good practice to use it in modern C++ programming. It's hard to understand and it's easy to change accidentally. For example, in your code, you use the label A: to jump from the end of the for loop to the end of the function. It would