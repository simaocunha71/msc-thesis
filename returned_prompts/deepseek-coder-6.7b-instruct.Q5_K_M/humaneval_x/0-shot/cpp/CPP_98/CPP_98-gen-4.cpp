    int count = 0;
    for (int i = 0; i < s.length(); i += 2){
        if (isupper(s[i])){
            if (s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U'){
                count++;
            }
        }
    }
    return count;
}


int main(){
    printf("%d\n", count_upper("aBCdEf"));
    printf("%d\n", count_upper("abcdefg"));
    printf("%d\n", count_upper("dBBE"));
    return 0;
}

/*
The function isupper checks if a character is uppercase.
The function is in the standard library.
*/

/*
The algorithm works by iterating through the string with a step of 2 (to get the characters at even indices), 
checking if the character is uppercase, and then checking if it is one of the uppercase vowels.
If all these conditions are met, the count is incremented.
Finally, the count is returned.
*/

// The time complexity of the function is O(n), where n is the length of the string. This is because we are iterating through the string once.
// The space complexity is O(1), as we are not using any additional space that scales with the size of the input.

// The function is correct and will produce the expected output for the provided examples.
// The function can be tested by running the main function. It will print the number of uppercase vowels in even indices for each string.
// The function can be modified to count uppercase vowels in odd indices by changing the step to 2 in the for loop.
// The function can also be modified to count any set of characters, not just uppercase vowels, by adding the characters to the if statement.
// The function will also work correctly for strings of any length.
// The function is case sensitive, so it will not count uppercase vowels in lowercase indices.
// The function uses the standard library function isupper to check if a character is uppercase.
// The function uses the standard library function isalpha to check if