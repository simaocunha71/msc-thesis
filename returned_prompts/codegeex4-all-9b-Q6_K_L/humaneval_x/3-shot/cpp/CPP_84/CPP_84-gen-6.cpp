
First off, your code is missing the function definitions for the three problems you posed, and the actual problem description.  I've included those below.
Now, let's look at your code.
You've included three functions, but you've not provided any test cases.  I'm not sure how you're going to test them.
It is generally better to use std::abs in C++ than to use the abs() function from the C standard library.  std::abs is a template function, and works on any numeric type.
You've defined three different problems with similar solutions, but different test cases.  You should consider creating a class to encapsulate the solution to each problem.
The first problem is pretty simple.  You've got a vector of numbers, and you want to know if any two numbers are within a given threshold of each other.  If you sort the vector first, you can then simply check adjacent pairs.  Here's an example implementation:
#include <vector>
#include <algorithm>
#include <cmath>

class CloseElements {
public:
    bool has_close_elements(const std::vector<float>& numbers, float threshold) const {
        std::vector<float> sorted = numbers;
        std::sort(sorted.begin(), sorted.end());
        for (std::size_t i = 1; i < sorted.size(); ++i) {
            if (std::abs(sorted[i] - sorted[i-1]) < threshold) {
                return true;
            }
        }
        return false;
    }
};

The second problem is about parsing a string of parentheses and extracting each individual group.  You're already using std::vector to store the groups, which is good.  Your code is mostly correct, but you're not handling the case where the string ends with an open parenthesis.  This can be fixed with a simple test after the loop:
#include <string>
#include <vector>
#include <cctype>

class Parentheses {
public:
    std::vector<std::string> separate_paren_groups(const std::string& paren_string) const {
        std::vector<std::string> all_parens;
        std::string current_paren;
       