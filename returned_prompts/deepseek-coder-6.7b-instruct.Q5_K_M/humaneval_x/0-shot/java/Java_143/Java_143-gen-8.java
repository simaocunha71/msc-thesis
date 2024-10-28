        String[] words = sentence.split(" ");
        StringBuilder sb = new StringBuilder();

        for(String word : words) {
            if(isPrime(word.length())) {
                sb.append(word + " ");
            }
        }

        return sb.toString().trim();
    }

    public boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i < n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

}

public class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution s = new Solution();
        System.out.println(s.wordsInSentence("This is a test"));
        System.out.println(s.wordsInSentence("lets go for swimming"));
    }
}

```

The code is a java program that takes a string and returns another string with words of prime length. The wordsInSentence method takes a string and splits it into words. Then it iterates over each word, checks if the length of the word is a prime number and if so, it appends it to a StringBuilder. Finally, it returns the string without the trailing space.

The isPrime method takes an integer and checks if it is a prime number by iterating from 2 to n and checking for divisors. If it finds one, it returns false, otherwise it returns true.

The main method tests the wordsInSentence method with two test cases: "This is a test" and "lets go for swimming". The results are printed to the console.

The time complexity of this solution is O(n^2) because of the nested loop in the isPrime method. The space complexity is O(n) because of the space required to store the words and the StringBuilder.




























































