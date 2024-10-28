        int sum = 0;
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(Character.isUpperCase(c))
                sum += (int) c;
        }
        return sum;
    }
}


A: The question is asking to find the sum of the ASCII values of all the uppercase characters in the string. 

The Character class has a static method named isUpperCase() which checks if a character is uppercase or not.
If the character is an uppercase letter, we convert it to its ASCII value using the int() cast and add it to the sum.

The final sum is returned.

In your example, the ASCII values of "A", "B", "C", "E" are 65, 66, 67, 69 respectively. So, the sum is 65 + 66 + 67 + 69 = 299.

The function digitSum("abAB") returns the sum of ASCII values of "A" and "B", which is 65 + 66 = 131.

Therefore, the function is working correctly.

Remember that, in ASCII table, uppercase letters 'A' to 'Z' are represented with numbers 65 to 90 respectively.


A: The question is asking to find the sum of ASCII values of all uppercase characters in the string.

The Character class has a static method named isUpperCase() which checks if a character is uppercase or not.
If the character is an uppercase letter, we convert it to its ASCII value using the int() cast and add it to the sum.

The final sum is returned.

In your example, the ASCII values of "A", "B", "C", "E" are 65, 66, 67, 69 respectively. So, the sum is 65 + 66 + 67 + 69 = 299.

The function digitSum("abAB") returns the sum of ASCII values of "A" and "B", which is 65 + 66 = 131.

Therefore, the function is working correctly.

Remember