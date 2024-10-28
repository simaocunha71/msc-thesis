        List<String> words = Arrays.asList(sentence.split(" "));
        List<String> prime_words = new ArrayList<>();
        for (String word : words) {
            if (isPrime(word.length())) {
                prime_words.add(word);
            }
        }
        return String.join(" ", prime_words);
    }

    private boolean isPrime(int number) {
        if (number <= 1) return false;
        for (int i = 2; i * i <= number; i++) {
            if (number % i == 0) return false;
        }
        return true;
    }
}


public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(solution.truncateNumber(3.5));
        System.out.println(solution.wordsInSentence("This is a test"));
        System.out.println(solution.wordsInSentence("lets go for swimming"));
    }
}
```