    int count = 0;
    for (int i = 0; i < str.size(); i++){
        if (str[i] == '['){
            count++;
        }
        else if (str[i] == ']'){
            count--;
        }
        if (count > 1){
            return true;
        }
    }
    return false;
}


int main() {
    printf("%d",is_nested("[[]]"));
    printf("%d",is_nested("[]]]]]]][[[[[]"));
    printf("%d",is_nested("[][]"));
    printf("%d",is_nested("[]"));
    printf("%d",is_nested("[[][]]"));
    printf("%d",is_nested("[[]][["));
    return 0;
}
// I used the C++ programming language. The function works by counting the number of open and closed brackets in the string.
// If the count ever goes above 1, then there is at least one bracket that is nested, so the function returns true.
// If the count never goes above 1, then there are no nested brackets, so the function returns false.
// The main function is used to test the function with different inputs.
// The expected output of the function is shown in the comments.
// The actual output of the function is shown in the console.
// If the actual output matches the expected output, then the function is working correctly.
// If the actual output does not match the expected output, then there is an error in the function.
// The function is_nested will return true if there is at least one nested bracket in the string, and false otherwise.
// The time complexity of the function is O(n), where n is the length of the string.
// The space complexity of the function is O(1), because no additional space is used that scales with the size of the input.
// The function assumes that the input string contains only square brackets. If this is not the case, the function may not work correctly.
// The function does not handle any errors that may occur if the input string contains characters other than square brackets.
// If this is a possibility, then the function should be modified to