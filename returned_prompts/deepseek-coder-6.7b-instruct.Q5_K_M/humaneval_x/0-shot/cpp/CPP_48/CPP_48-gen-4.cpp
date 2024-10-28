    int len = text.size();
    for(int i=0; i<len/2; i++){
        if(text[i] != text[len-i-1]){
            return false;
        }
    }
    return true;
}

int main(){
    string text;
    printf("Enter string: ");
    getline(cin, text);
    if(is_palindrome(text)){
        printf("true");
    }else{
        printf("false");
    }
    return 0;
}

// Test Cases:
// is_palindrome("") => true
// is_palindrome("aba") => true
// is_palindrome("aaaaa") => true
// is_palindrome("zbcd") => false

// Note: This code is written in C++ and it takes a string as input from the user and checks if it is a palindrome. If it is, it returns true; otherwise, it returns false.

// Time Complexity: O(n)
// Space Complexity: O(1)

// Where n is the length of the string.

// This is because we are traversing the string only once. So, the time complexity is O(n).
// The space complexity is O(1) because we are not using any extra space that scales with the input size.
// We only use a few variables and a loop counter, so the space complexity is constant.

// This code is simple and efficient.

// This code can be further optimized by eliminating the use of the getline() function and by using the cin.eof() function to handle the end of file condition.
// This will make the code more robust and can be used in a larger program.
// Also, the code can be further optimized by eliminating the use of the getline() function and by using the cin.eof() function to handle the end of file condition.
// This will make the code more robust and can be used in a larger program.

// Note: This code is written in C++ and it takes a string as input from the user and checks if it is a palindrome. If it is, it returns true; otherwise, it returns false.

// Time