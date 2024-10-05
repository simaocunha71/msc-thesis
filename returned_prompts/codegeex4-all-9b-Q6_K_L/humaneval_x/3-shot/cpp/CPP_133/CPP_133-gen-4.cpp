
The first function you provided has a bug. Consider the following code:
int main()
{
    vector<float> numbers = {1.0f, 2.0f, 3.0f};
    bool result = has_close_elements(numbers, 0.5f);
    return 0;
}

The function has_close_elements will return true, because there are two numbers in the list that are exactly 1.0 apart. However, this is not what you want. You want to check if there are any two numbers that are closer to each other than the threshold. The correct code should be:
bool has_close_elements(vector<float> numbers, float threshold)
{
    int i, j;
    for (i = 0; i < numbers.size(); i++)
    {
        for (j = i + 1; j < numbers.size(); j++)
        {
            if (fabs(numbers[i] - numbers[j]) < threshold)
            {
                return true;
            }
        }
    }
    return false;
}

The second function you provided is correct. It separates the groups of parentheses into separate strings and returns the vector of those.

The third function you provided is correct. It returns the decimal part of the number.

The fourth function you provided is correct. It returns the sum of squared numbers in the list, after rounding each element to the upper int(Ceiling) first.