    vector<int> result;
    for(int i=0; i<numbers.size(); i++) {
        result.push_back(numbers[i]);
        if(i < numbers.size()-1) {
            result.push_back(delimeter);
        }
    }
    return result;
}

The function works by iterating over each element in the input vector `numbers". For each element, it adds the element to a new vector `result" and then adds the delimeter to the new vector. This process is repeated until the last element in the vector `numbers". The new vector `result" is then returned. If the vector `numbers" is empty, the function will return an empty vector.

The time complexity of this function is O(n), where n is the size of the input vector `numbers". This is because the function iterates over each element in the vector once. The space complexity is also O(n), as the function creates a new vector that is at most twice the size of the input vector.

Test the function with the given examples:

>>> intersperse({}, 4)
{}

>>> intersperse({1, 2, 3}, 4)
{1, 4, 2, 4, 3}
*/





































































































































