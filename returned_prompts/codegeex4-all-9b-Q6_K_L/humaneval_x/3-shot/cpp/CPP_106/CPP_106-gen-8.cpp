
For the first question, your solution is correct, but you can write it more efficiently. Since you don't need to compare all pairs, but only adjacent ones, you can use a single loop. Also, you don't need to use abs since you are comparing to a positive number:
bool has_close_elements(vector<float> numbers, float threshold)
{
    for (size_t i = 1; i < numbers.size(); ++i)
        if (