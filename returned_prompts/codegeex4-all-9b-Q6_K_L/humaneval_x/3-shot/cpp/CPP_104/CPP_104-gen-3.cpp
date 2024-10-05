
Use the Standard Library
You are using C-style for loops and other C++ standard library features. Use the standard library. It is designed to work with the C++ language. For example, use std::abs instead of abs.
Use a range-based for loop
Instead of a C-style for loop, use a range-based for loop. It is much easier to read.
Use std::string::find instead of a for loop
Instead of a for loop to find the first closing parenthesis, use std::string::find. It will return the position of the first closing parenthesis. If it is not found, it will return std::string::npos.
Use std::vector::emplace_back instead of std::vector::push_back
Instead of std::vector::push_back, use std::vector::emplace_back. It is more efficient because it does not require a copy or move of the element.
Use std::string::substr instead of a string copy
Instead of copying the substring into a new string, use std::string::substr. It returns a new string that is a substring of the original string.
Use std::vector::erase instead of a for loop
Instead of a for loop to remove elements from the vector, use std::vector::erase. It removes the elements and updates the size of the vector.
Use std::remove_if instead of a for loop
Instead of a for loop to remove elements from the vector, use std::remove_if. It removes the elements and updates the size of the vector.
Use std::find_if instead of a for loop
Instead of a for loop to find an element in the vector, use std::find_if. It returns an iterator to the first element that matches the predicate.
Use std::unique instead of a for loop
Instead of a for loop to remove duplicates from the vector, use std::unique. It removes the duplicates and updates the size of the vector.
Use std::sort instead of a for loop
Instead of a for loop to sort the vector, use