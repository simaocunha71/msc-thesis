        char[] wordChars = word.toCharArray();
        int left = 0, right = word.length() - 1;
        while (wordChars[left] == 'a' || wordChars[left] == 'e' ||
               wordChars[left] == 'i' || wordChars[left] == 'o' ||
               wordChars[left] == 'u' || wordChars[left] == 'A' ||
               wordChars[left] == 'E' || wordChars[left] == 'I' ||
               wordChars[left] == 'O' || wordChars[left] == 'U') {
            left++;
        }
        while (wordChars[right] == 'a' || wordChars[right] == 'e' ||
               wordChars[right] == 'i' || wordChars[right] == 'o' ||
               wordChars[right] == 'u' || wordChars[right] == 'A' ||
               wordChars[right] == 'E' || wordChars[right] == 'I' ||
               wordChars[right] == 'O' || wordChars[right] == 'U') {
            right--;
        }
        for (int i = left + 1; i < right; i++) {
            if (wordChars[i] == 'a' || wordChars[i] == 'e' ||
                wordChars[i] == 'i' || wordChars[i] == 'o' ||
                wordChars[i] == 'u' || wordChars[i] == 'A' ||
                wordChars[i] == 'E' || wordChars[i] == 'I' ||
                wordChars[i] == 'O' || wordChars[i] == 'U') {
                return String.valueOf(wordChars[i]);
            }
        }
        return "";
    }
}
















































