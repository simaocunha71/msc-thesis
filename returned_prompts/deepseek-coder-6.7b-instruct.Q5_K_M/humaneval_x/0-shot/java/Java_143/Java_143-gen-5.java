        StringBuilder sb = new StringBuilder();
        List<String> words = Arrays.asList(sentence.split(" "));
        for (String word : words) {
            if (isPrime(word.length())) {
                sb.append(word).append(" ");
            }
        }
        return sb.toString().trim();
    }

    private boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}

In this code, the function wordsInSentence splits the input sentence into words and checks each word's length. If the length is a prime number, it appends the word to the string builder. The function isPrime checks if a given number is prime by iterating from 2 to the square root of the number. If the number is divisible by any of these numbers, it is not prime.

In the example "This is a test", the word "is" has length 2, which is a prime number, so it gets appended to the string builder. The other words "This", "a", "test" have lengths that are not prime numbers, so they are not appended.

In the example "lets go for swimming", the words "go", "for" have lengths that are prime numbers, so they get appended to the string builder. The other words "lets", "swimming" have lengths that are not prime numbers, so they are not appended.

The time complexity of the code is O(n*m), where n is the number of words in the sentence and m is the average length of the words. The space complexity is O(n), where n is the number of words in the sentence.
