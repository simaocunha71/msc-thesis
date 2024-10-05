
The first question has some problems:

The loop variable i is not needed. The outer loop is unnecessary.
The inner loop variable j is also unnecessary. The loop can be combined with the outer loop.
The if statement should be an if-else if statement to prevent false positives.
The return statement should be outside the inner loop.

Here's the corrected code:
bool has_close_elements(vector<float> numbers, float threshold){
    for (int i = 0; i < numbers.size(); i++){
        for (int j = i + 1; j < numbers.size(); j++){
            if (abs(numbers[i] - numbers[j]) < threshold){
                return true;
            }
        }
    }
    return false;
}

The second question is fine.

The third question has a problem:
The return statement should return the truncated number, not the result of the comparison.
Here's the corrected code:
float truncate_number(float number){
    return number - int(number);
}

The fourth question has some problems:

The sort function is unnecessary. The vector can be returned as is.
The return statement should be outside the if statement.

Here's the corrected code:
vector<int> maximum(vector<int> arr, int k){
    sort(arr.begin(), arr.end());
    return vector<int>(arr.end() - k, arr.end());
}