
The first function has a logical error. If you have a threshold of 0.5 and two numbers of 1.0 and 1.5, it should return true, but because 1.5 - 1.0 is not less than 0.5, it returns false.
You can fix this by adding a condition that checks if the numbers are equal. If they are equal, return true.
bool has_close_elements(vector<float> numbers, float threshold){
    for (int i = 0; i < numbers.size(); i++)
        for (int j = i + 1; j < numbers.size(); j++)
            if (abs(numbers[i] - numbers[j]) < threshold || numbers[i] == numbers[j])
                return true;
    return false;
}

The second function is correct. It correctly separates the groups of parentheses into separate strings.

The third function is correct. It correctly returns the decimal part of the number.

The fourth function has a logical error. If you have a score of 1 and a guess of 2, the absolute difference is 1, but it should be 1. If you have a score of 1 and a guess of -1, the absolute difference is 2, but it should be 1. You can fix this by dividing the absolute difference by 2.
vector<int> compare(vector<int> game, vector<int> guess){
    vector<int> results;
    for (int i = 0; i < game.size(); i++)
        results.push_back(abs(game[i] - guess[i]) / 2);
    return results;
}