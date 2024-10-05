
There are a few things to note about your code:

You are using the C++ standard namespace in your includes, but then not using the namespace qualifier in your code. You should either remove the using namespace std; line or qualify the namespace in your code.
You are mixing C and C++ style includes. You should stick to either C or C++ style includes. For example, #include <stdio.h> is a C style include. It is better to use the C++ style include, which is #include <cstdio>. 

Here is your code with some changes:

/*
Check if in given vector of numbers, are any two numbers closer to each other than
given threshold.
>>> has_close_elements({1.0, 2.0, 3.0}, 0.5)
false
>>> has_close_elements({1.0, 2.8, 3.0, 4.0, 5.0, 2.0}, 0.3)
true
*/
#include <vector>
#include <cmath>
#include <cstdio>

using namespace std;

bool has_close_elements(vector<float> numbers, float threshold) {
    int i, j;

    for (i = 0; i < numbers.size(); i++)
        for (j = i + 1; j < numbers.size(); j++)
            if (abs(numbers[i] - numbers[j]) < threshold)
                return true;

    return false;
}

/*
Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
separate those group into separate strings and return the vector of those.
Separate groups are balanced (each open brace is properly closed) and not nested within each other
Ignore any spaces in the input string.
>>> separate_paren_groups("( ) (( )) (( )( ))")
{"()", "(())", "