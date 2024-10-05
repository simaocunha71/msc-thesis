
A lot of your questions are very similar in structure, so I'll go through the first one and you can compare it to the others.
In your has_close_elements function, you are using a goto statement to jump to the label A: at the end of the function.  This is not recommended as it makes the code hard to follow and debug.  You should be able to get rid of that and just use a simple return statement.
Also, you are using the abs function from the math library to calculate the absolute difference between two numbers.  This is fine, but you could also use the fabs function from the cmath library.  The only difference between the two is that abs is a macro that evaluates its argument multiple times, whereas fabs is a function that only evaluates its argument once.  This is more efficient, but since the argument is already a simple subtraction, it doesn't really matter.
Here's my version of your function:
bool has_close_elements(vector<float> numbers, float threshold){
    for (int i = 0; i < numbers.size(); i++)
        for (int j = i + 1; j < numbers.size(); j++)
            if (fabs(numbers[i] - numbers[j]) < threshold)
                return true;
    return false;
}

In your separate_paren_groups function, you are using the char type to store characters.  This is fine, but you could also use the char16_t type from the cstdint