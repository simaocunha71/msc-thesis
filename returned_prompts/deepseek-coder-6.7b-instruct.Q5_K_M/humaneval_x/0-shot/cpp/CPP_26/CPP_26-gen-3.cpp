    sort(numbers.begin(), numbers.end());
    vector<int>::iterator it;
    for(it = numbers.begin(); it != numbers.end(); ++it){
        if(count(numbers.begin(), numbers.end(), *it) > 1){
            it = numbers.erase(it);
        }
    }
    return numbers;
}

int main() {
    vector<int> numbers = {1, 2, 3, 2, 4};
    numbers = remove_duplicates(numbers);
    for(int i=0; i<numbers.size(); i++)
        printf("%d ", numbers[i]);
    return 0;
}

Explanation:
The function remove_duplicates() is taking a vector of integers as input. Inside this function, we are first sorting the vector. Then, we are using a for loop to iterate through the vector. Inside this loop, we are using the count() function to count the number of times an element appears in the vector. If the count is more than 1, we are using the erase() function to remove that element from the vector. Finally, we are returning the modified vector.

The main() function is just for testing. It is creating a vector of integers, calling the remove_duplicates() function on this vector, and printing the result.
*/

