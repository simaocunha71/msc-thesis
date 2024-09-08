    vector<int> result(2,0);
    for(int i = 1; i <= n; i++){
        string temp = to_string(i);
        bool is_palindrome = true;
        for(int j = 0; j < temp.length(); j++){
            if(temp[j] != temp[temp.length()-1-j]){
                is_palindrome = false;
                break;
            }
        }
        if(is_palindrome){
            if(i % 2 == 0){
                result[0]++;
            }else{
                result[1]++;
            }
        }
    }
    return result;
}

int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    vector<int> res = even_odd_palindrome(n);
    printf("Even palindromes: %d\n", res[0]);
    printf("Odd palindromes: %d\n", res[1]);
    return 0;
}  // Time complexity: O(n log n), space complexity: O(1).  This solution works by iterating over all numbers from 1 to n, converting each number to a string, checking if it's a palindrome, and then incrementing the appropriate count in the result vector.  The time complexity is O(n log n) because string conversion and palindrome checking take O(log n) time each, and there are n numbers to process.  The space complexity is O(1) because we only use a constant amount of space to store the result vector and other variables.  This solution is not very efficient for large values of n, but it's simple and easy to understand.  For more efficient solutions, you could use a more clever algorithm or a more efficient data structure.  For example, you could use a hash set to store the palindromes and then count the number of even and odd palindromes in O(n) time.  However, this would require more complex code and might be harder to understand.  In practice, the choice of solution depends on the specific requirements and constraints of the problem.  If you need a fast solution and can use a more complex algorithm or data structure, then that might be a good choice.  If you need a simple solution and don't mind the extra time complexity, then this solution might be sufficient.  Ultimately, the choice of solution depends on your specific needs and constraints.  //  //  //  //  //  //  //  //  //  //