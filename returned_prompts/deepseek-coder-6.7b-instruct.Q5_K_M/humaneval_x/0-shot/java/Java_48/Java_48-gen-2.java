        int i = 0, j = text.length() - 1;
        while (i < j) {
            if (text.charAt(i) != text.charAt(j))
                return false;
            i++;
            j--;
        }
        return true;
    }
}

The above code checks if the input string is a palindrome by comparing the first and last characters, then the second and second last characters and so on until it reaches the middle of the string. If all the pairs are equal it returns true, else it returns false. This way it avoids unnecessary comparisons and improves efficiency.


