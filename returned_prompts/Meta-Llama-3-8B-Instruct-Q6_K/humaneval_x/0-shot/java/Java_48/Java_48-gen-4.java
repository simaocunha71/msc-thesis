        // Convert string to char array
        char[] charArray = text.toCharArray();

        // Initialize two pointers
        int left = 0;
        int right = charArray.length - 1;

        // Loop until left pointer meets right pointer
        while (left < right) {
            // If characters at left and right pointers are different, return false
            if (charArray[left] != charArray[right]) {
                return false;
            }

            // Move pointers towards the center of the string
            left++;
            right--;
        }

        // If loop finishes without returning false, string is a palindrome
        return true;
    }
}

