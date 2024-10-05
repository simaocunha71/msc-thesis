
has_close_elements

There is a simpler way to do this using std::sort and std::adjacent_find:

bool has_close_elements(vector<float> numbers, float threshold){
    std::sort(numbers.begin(), numbers.end());
    return std::adjacent_find(numbers.begin(), numbers.end(), std::less<float>(threshold)) != numbers.end();
}

separate_paren_groups

In the first iteration of the for loop, you are trying to access the first character of the string. This is probably not what you want. I would suggest using std::istringstream to parse the string.

vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    std::istringstream iss(paren_string);
    char ch;
    while (iss >> std::noskipws >> ch) {
        // ...
    }
    return all_parens;
}

truncate_number

You can use std::modf to split the number into the integer and fractional parts.

float truncate_number(float number){
    int integer_part;
    float fractional_part = std::modf(number, &integer_part);
    return fractional_part;
}

can_arrange

You can use std::is_sorted to check if the array is sorted. If it is sorted, return -1. If it is not sorted, return the index of the first element that is not greater than or equal to the element immediately preceding it.

int can_arrange(vector<int> arr){
    if (std::is_sorted(arr.begin(), arr.end())) {
        return -1;
    }
    for (int i = 0; i < arr.size() - 1; ++i) {
        if (arr[i] > arr[i + 1]) {
            return i;
        }
    }
    return -1;
}