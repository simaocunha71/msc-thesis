    vector<int> result;

    sort(numbers.begin(), numbers.end());

    for(int i = 0; i < numbers.size(); i++){
        if(i == numbers.size()-1 || numbers[i] != numbers[i+1]){
            result.push_back(numbers[i]);
        }
    }
    return result;
}

int main(){
    vector<int> test = {1, 2, 3, 2, 4};
    vector<int> result = remove_duplicates(test);

    for(int i=0; i< result.size(); i++)
        printf("%d ", result[i]);

    return 0;
}

*/

//
// This is code is a solution to the above problem. It removes the duplicates from the input vector and keeps the order of elements as it was in the input.
// It uses the sort function to sort the vector first and then it checks for the duplicates.
// If the element is not a duplicate, it is pushed into the result vector.
// The main function tests the remove_duplicates function.
//
// Time Complexity: O(n log n) due to sorting
// Space Complexity: O(n)
//
// Where, n is the size of the input vector.
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//