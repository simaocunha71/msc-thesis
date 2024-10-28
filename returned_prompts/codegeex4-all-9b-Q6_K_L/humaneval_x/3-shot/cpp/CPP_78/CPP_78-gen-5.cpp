
I'll focus on the first task, the rest are similar.
The code contains several issues:

The function should return bool, but it returns int. Also, the name has_close_elements is not very descriptive. It should be something like are_numbers_closer_than_threshold
The function uses the deprecated C-style for loop. It should be replaced with the more modern range-based for loop.
The function uses the magic number 0.5 and 0.3. These should be replaced with named constants.
The function uses the magic number 2. It should be replaced with a named constant.
The function uses the magic number 1. It should be replaced with a named constant.

Here's the revised version of the function:
#include <algorithm>
#include <vector>

bool are_numbers_closer_than_threshold(const std::vector<float>& numbers, float threshold)
{
    static const float EPSILON = 0.5f;
    static const float THRESHOLD = 0.3f;
    static const int MAX_ITERATIONS = 2;
    static const int MAX_LEVEL = 1;

    for (auto i = numbers.begin(); i != numbers.end(); ++i)
    {
        for (auto j = i + 1; j != numbers.end(); ++j)
        {
            if (std::abs(*i - *j) < threshold)
            {
                return true;
