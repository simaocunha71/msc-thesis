        Set<Integer> prime = new TreeSet<>();
        for(int i = 2; i <= 100; i++) {
            if(isPrime(i)) {
                prime.add(i);
            }
        }

        List<String> words = Arrays.asList(sentence.split(" "));
        List<String> primeWords = new ArrayList<>();

        for(String word : words) {
            if(prime.contains(word.length())) {
                primeWords.add(word);
            }
        }

        return String.join(" ", primeWords);
    }

    public boolean isPrime(int num) {
        if(num == 2) {
            return true;
        }
        if(num % 2 == 0) {
            return false;
        }
        for(int i = 2; i*i <= num; i++) {
            if(num % i == 0) {
                return false;
            }
        }
        return true;
    }
}

































































































































































































































































