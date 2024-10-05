
First of all, there's a lot of code you've shown that doesn't even belong to the problems you've posted. I'll ignore all the other code and focus only on the code that's related to the problems you've asked for.

This is the first problem you've asked for. The code you've written is correct, but there are some things that could be improved:

The code is not very efficient. You're iterating over the entire vector twice. This is not necessary. You can iterate over the vector once and keep track of the minimum value you've seen so far. If the current value is less than the minimum value you've seen so far, then you have a pair of close numbers.
The function name has_close_elements is not very descriptive. It's better to name it something that clearly indicates what the function does. For example, has_close_pair.
The function name should be in camelCase, not snake_case.
The function should return void, not bool. The caller of the function should decide what to do with the result.
The function should take a const reference to the vector, not a copy of the vector. This is to avoid unnecessary copying and to avoid modifying the vector.

Here's a revised version of the function:

bool has_close_pair(const vector<float>& numbers, float threshold)
{
    if (numbers.size() < 2)
    {
        return false;
    }

    float min_value = numbers[0];
    for (size_t i = 1; i < numbers.size(); ++i)
    {
        if (numbers[i] < min_value)
        {
            min_value = numbers[i];
        }
        else if (numbers[i] - min_value < threshold)
        {
            return true;
        }
    }

    return false;
}

Now, let's move on to the second problem.

This is the second problem you've asked for. The code you've written is mostly correct, but there are some things that could be improved:

The code is not very efficient. You're iterating over the entire vector twice. This is not necessary. You can iterate over the vector once and keep track of the current level of nesting. If the current level is 0 and you encounter a closing parenthesis, then you have a complete group of parentheses.
The function name separate_p