
has_close_elements
First of all, you have a label A: that is not used.  You can remove that.
Secondly, your code is inefficient because it compares every pair of numbers.  You can improve the performance by only comparing each number with its neighbors.
Lastly, your function does not handle the case where the vector is empty.  This could cause a segmentation fault if you pass an empty vector to your function.
Here is a more efficient version of the function:
bool has_close_elements(vector<float> numbers, float threshold){
    if (numbers.empty()) {
        return false;
    }

    for (size_t i = 0; i < numbers.size() - 1; ++i) {
        if (abs(numbers[i] - numbers[i+1]) < threshold) {
            return true;
        }
    }

    return false;
}

separate_paren_groups
Your code is correct, but it is not very efficient.  You are iterating through the string twice: once to calculate the level, and once to build the current_paren string.  You can combine these two loops into one.
Here is a more efficient version of the function:
vector<string> separate_paren