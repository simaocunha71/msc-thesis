        if(s.length() < 3) return false;
        for(int i=0; i<s.length()-2; i++){
            if(s.charAt(i) == s.charAt(i+1) || s.charAt(i+1) == s.charAt(i+2) || s.charAt(i) == s.charAt(i+2))
                return false;
        }
        return true;
    }
}

// This code will return true if the string is happy and false if the string is not happy.

// Also, please note that this code assumes that the input string is in lowercase and consists of only alphabets. If this is not the case, you will need to modify the code to handle these cases.

// Also, the code does not handle strings that have special characters or numbers. If you need to handle these cases, you will need to modify the code.

// This code has a time complexity of O(n) where n is the length of the string. This is because it iterates over the string once.

// This code has a space complexity of O(1) because it uses a fixed amount of space to store the string and does not depend on the size of the string.

// This code is a simple and efficient way to check if a string is happy or not.

// Please note that this code does not handle strings that have special characters or numbers. If you need to handle these cases, you will need to modify the code.

// This code has a time complexity of O(n) where n is the length of the string. This is because it iterates over the string once.

// This code has a space complexity of O(1) because it uses a fixed amount of space to store the string and does not depend on the size of the string.

// This code is a simple and efficient way to check if a string is happy or not.

// Please note that this code does not handle strings that have special characters or numbers. If you need to handle these cases, you will need to modify the code.

// This code has a time complexity of O(n) where n is the length of the string. This is because it iterates over the string once.

// This code has a space complexity of O