    vector<int> result(2, 0);
    for(int i = 1; i <= n; i++){
        string str = to_string(i);
        bool is_palindrome = true;
        for(int j = 0; j < str.length(); j++){
            if(str[j] != str[str.length() - 1 - j]){
                is_palindrome = false;
                break;
            }
        }
        if(is_palindrome && i % 2 == 0){
            result[0]++;
        } else if(is_palindrome && i % 2 != 0){
            result[1]++;
        }
    }
    return result;
}

int main(){
    int n = 12;
    vector<int> result = even_odd_palindrome(n);
    for(int i = 0; i < result.size(); i++){
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
}

Solution:
The solution is to iterate over all integers from 1 to n, convert each integer to a string, and check if the string is a palindrome. If it is, increment the corresponding counter in the result vector. The counter at index 0 is for even palindromes, and the counter at index 1 is for odd palindromes.

In the main function, we test the solution with n = 12 and print the result.

The time complexity is O(n * log n) due to the conversion of integers to strings, and the space complexity is O(1) as we only use a constant amount of space.