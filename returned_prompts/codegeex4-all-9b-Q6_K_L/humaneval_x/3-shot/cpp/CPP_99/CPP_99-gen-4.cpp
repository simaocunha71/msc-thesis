
For the first question, there are some issues with your loop.  Here's how I'd do it:
bool has_close_elements(vector<float> numbers, float threshold){
    for (unsigned i = 0; i < numbers.size(); ++i) {
        for (unsigned j = i + 1; j < numbers.size(); ++j) {
            if (abs(numbers[i] - numbers[j]) < threshold) {
                return true;
            }
        }
    }
    return false;
}

You were missing the ++ on the for loop iterators, and you were not using unsigned types, which is a good idea when dealing with array sizes.

For the second question, your code looks good, but you could add some comments to explain what the code is doing.

The third question is easy enough to implement:
float truncate_number(float number) {
    return number - floor(number);
}

And for the last question, I'd use the standard library's round function:
#include <cmath>

int closest_integer(string value) {
    return round(atof(value.c_str()));
}