    int sum = 0;
    int n = q.size();
    for(int i = 0; i < n; i++)
        sum += q[i];
    if(sum > w)
        return false;
    for(int i = 0; i < n / 2; i++)
        if(q[i] != q[n - i - 1])
            return false;
    return true;
}

int main(){
    printf("%s\n", will_it_fly({1, 2}, 5)? "true":"false");
    printf("%s\n", will_it_fly({3, 2, 3}, 1)? "true":"false");
    printf("%s\n", will_it_fly({3, 2, 3}, 9)? "true":"false");
    printf("%s\n", will_it_fly({3}, 5)? "true":"false");
    return 0;
}

*/

//The C++ program is a function that takes an array of integers and a maximum weight as inputs, and returns whether the object will fly. It checks if the sum of the elements is less than or equal to the maximum weight, and if the array is a palindrome. If both conditions are met, it returns true, otherwise it returns false.
//The function works by first initializing a variable sum to 0, then adding up all the elements in the array. If the sum is greater than the maximum weight, it immediately returns false.
//Next, the function checks if the array is a palindrome. It does this by iterating over the array from both ends, and if it finds any pair of elements that are not equal, it immediately returns false.
//If the array passes both checks, the function returns true.
//The main function is used to test the will_it_fly function with different inputs.
//The output of the main function is a series of "true" or "false" values, indicating whether the object will fly for each input.
//The complexity of this function is O(n), as it needs to iterate over the array twice: once to calculate the sum, and once to check if the array is a palindrome.
//The space complexity is O(1), as it only needs