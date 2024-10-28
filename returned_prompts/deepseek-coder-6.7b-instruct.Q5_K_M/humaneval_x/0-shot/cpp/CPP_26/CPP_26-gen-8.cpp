    vector<int> result;
    sort(numbers.begin(), numbers.end());
    for (size_t i = 0; i < numbers.size(); ++i){
        if (i == numbers.size() - 1 || numbers[i] != numbers[i + 1]){
            result.push_back(numbers[i]);
        }
    }
    return result;
}
int main(){
    vector<int> numbers = {1, 2, 3, 2, 4};
    vector<int> result = remove_duplicates(numbers);
    for(int i=0; i<result.size(); i++){
        printf("%d ",result[i]);
    }
    return 0;
}

This program takes a vector of integers and removes all elements that occur more than once. It also keeps the order of elements the same as in the input. It uses the STL algorithm sort() to sort the vector and then iterates over the vector to check for duplicates. If the current element is not equal to the next one, it is added to the result vector.
*/

// Answer:
/*
The given program is correct and it will work as expected. It sorts the input vector and then iterates over the sorted vector. For each element, it checks if it is the last element or if it is different from the next element. If the condition is true, it means the element is not a duplicate and it is added to the result vector.

After the loop, the function returns the result vector. The main function prints the elements of the result vector.
*/

// Time Complexity:
/*
The time complexity of the program is O(n log n) due to the sorting operation. The iteration over the vector is O(n). Therefore, the overall time complexity is O(n log n).
*/

// Space Complexity:
/*
The space complexity of the program is O(n) as we are using an additional vector to store the result. The size of the result vector is proportional to the size of the input vector. Therefore, the space complexity is O(n).
*/

// Test Cases:
/*
The program is tested with the provided test case {1, 2, 3, 2, 