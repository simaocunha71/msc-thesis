
First of all, you're not using the standard library's algorithms, which is a good thing. But you're also not using the standard library's functions, which is not so good. This is a problem of "what's available" versus "what's standard".
For example, in the code:
for (i=0;i<paren_string.length();i++)

You're using a pre-C++11 construct. In C++11, you can do:
for (auto i = paren_string.begin(); i != paren_string.end(); ++i)

And for the second question, you're doing:
for (i=0;i<numbers.size();i++)
for (j=i+1;j<numbers.size();j++)

Here, you're using a pre-C++11 construct. In C++11, you can do:
for (auto i = numbers.begin(); i != numbers.end(); ++i)
for (auto j = i+1; j != numbers.end(); ++j)

In all three cases, you're using a pre-C++11 construct. In C++11, you can do:
for (auto i : numbers)
for (auto j : numbers)

You're also using the old C style for loop. C++11 introduced the range-based for loop, which is much nicer. It's also more expressive, and you don't have to remember the range of the loop. The range-based for loop also lets you use the const keyword to make sure you don't modify the elements of the container.
In addition, you're using a pre-C++11 feature of the standard library, the abs function. In C++11, you can use the standard library's abs function:
#include <cmath>
auto value = abs(a - b);

In the third question, you're using a pre-C++11 construct. In C++11, you can do:
for (auto i : arr)

And for the sort_array function, you're using the old C style for loop. C++11 introduced the range-based for loop, which is much nicer. It's also more expressive, and you don't have to remember the range of the loop. The range-based for loop also lets you use the const keyword to make sure you don't modify the elements of the container.
In addition, you're using the old C style for loop. C++11 introduced the range-based for loop, which is much nicer. It's also more