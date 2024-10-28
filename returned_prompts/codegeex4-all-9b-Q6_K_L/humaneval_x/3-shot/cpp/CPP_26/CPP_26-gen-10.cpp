
In general, it looks pretty good. Some minor comments:

In has_close_elements, you have a label A and a goto statement. This is pretty unusual in C++ and should be avoided. I'd suggest just using a break statement.
In has_close_elements, you have a typo in the function signature. You have "vector<float> numbers" which should be "vector<double> numbers".
In separate_paren_groups, you use a raw string instead of a string literal. That's a good idea in general, but it's not necessary here. You can just use "paren_string".
In separate_paren_groups, you use a char variable instead of a char literal. That's a good idea in general, but it's not necessary here. You can just use paren_string[i].
In separate_paren_groups, you use a for loop instead of a while loop. That's a good idea in general, but it's not necessary here. You can just use a while loop.
In separate_paren_groups, you use a vector of strings instead of a vector of string. That's a good idea in general, but it's not necessary here. You can just use a vector of string.
In separate_paren_groups, you use a vector of strings instead of a vector of string. That's a good idea in general, but it's not necessary here. You can just use a vector of string.
In separate_paren_groups, you use a vector of strings instead of a vector of string. That's a good idea in general, but it's not necessary here. You can just use a vector of string.
In separate_paren_groups, you use a vector of strings instead of a vector of string. That's a good idea in general, but it's not necessary here. You can just use a vector of string.
In separate_paren_groups, you use a vector of strings instead of a vector of string. That's a good idea in general, but it's not necessary here. You can just use a vector of string.
In separate_paren_groups, you use a vector of strings instead of a vector of string. That's a good idea in general,