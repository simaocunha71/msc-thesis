        String vowels = "aeiouAEIOU";
        StringBuilder sb = new StringBuilder(word);
        String reversedWord = sb.reverse().toString();
        for (int i = 1; i < reversedWord.length() - 1; i++) {
            if (vowels.contains(String.valueOf(reversedWord.charAt(i))) &&
                !vowels.contains(String.valueOf(reversedWord.charAt(i - 1))) &&
                !vowels.contains(String.valueOf(reversedWord.charAt(i + 1)))) {
                return String.valueOf(reversedWord.charAt(i));
            }
        }
        return "";
    }
}

I:
    public static void main (String[] args) throws java.lang.Exception {
        Solution s = new Solution();
        System.out.println(s.getClosestVowel("yogurt")); //u
        System.out.println(s.getClosestVowel("FULL")); //U
        System.out.println(s.getClosestVowel("quick")); //(empty)
        System.out.println(s.getClosestVowel("ab")); //(empty)
    }
}

The method getClosestVowel is supposed to find the closest vowel between two consonants from the right side of the word.
The test cases check for words that have vowels between consonants, words that do not have vowels between consonants, and words with only one letter. The expected output is the vowel between consonants from the right side of the word. If there is no such vowel, it should return an empty string.
*/

// The method getClosestVowel is supposed to find the closest vowel between two consonants from the right side of the word.
// The test cases check for words that have vowels between consonants, words that do not have vowels between consonants, and words with only one letter. The expected output is the vowel between consonants from the right side of the word. If there is no such vowel, it should