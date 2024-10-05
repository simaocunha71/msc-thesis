    public String getClosestVowel(String word) {
        int rightIndex = word.length() - 1;
        while (rightIndex >= 0 && !isVowel(word.charAt(rightIndex))) {
            rightIndex--;
        }
        if (rightIndex < 0) {
            return "";
        }
        int leftIndex = rightIndex - 1;
        while (leftIndex >= 0 && !isVowel(word.charAt(leftIndex))) {
            leftIndex--;
        }
        if (leftIndex < 0) {
            return "";
        }
        return String.valueOf(word.charAt(leftIndex + 1));
    }

    private boolean isVowel(char ch) {
        ch = Character.toLowerCase(ch);
        return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
    }
}
Explanation:
The task is to find the closest vowel that stands between two consonants from the right side of the word. 

First, we start from the right side of the word and move towards the left until we find a vowel. If we don't find any vowel, we return an empty string. 

Then, we move towards the right from the found vowel until we find a consonant. The vowel that we found is the closest vowel that stands between two consonants. 

If we don't find any vowel that stands between two consonants, we return an empty string. 

The function `isVowel` is used to check if a character is a vowel or not. 

The time complexity is O(n) where n is the length of the word, as we are scanning the word from right to left and then from left to right. The space complexity is O(1), as we are not using any extra space that scales with the input. 





