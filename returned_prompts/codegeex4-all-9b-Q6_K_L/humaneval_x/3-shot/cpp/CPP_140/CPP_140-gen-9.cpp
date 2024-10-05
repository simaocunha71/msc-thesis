
The first question has a bug. You need to break out of the outer loop if you return true. Otherwise you will return true if any pair is closer than the threshold, not just the first one.
Also, this code is not very efficient. You are looping through the entire vector twice. You can just loop once and keep track of the minimum and maximum values seen so far. Then just check if the difference is less than the threshold.
Here's a cleaner version:
bool has_close_elements(vector<float> numbers, float threshold)
{
    float min_value = numbers[0];
    float max_value = numbers[0];

    for (int i = 1; i < numbers.size(); i++)
    {
        if (numbers[i] < min_value)
            min_value = numbers[i];
        else if (numbers[i] > max_value)
            max_value = numbers[i];
    }

    return (max_value - min_value) < threshold;
}