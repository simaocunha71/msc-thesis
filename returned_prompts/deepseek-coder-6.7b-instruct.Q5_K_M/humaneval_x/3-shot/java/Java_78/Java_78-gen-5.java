        Set<Character> primeDigits = new HashSet<Character>(Arrays.asList('2', '3', '5', '7', 'B', 'D'));
        int count = 0;
        for (char c : num.toCharArray()) {
            if (primeDigits.contains(c)) {
                count++;
            }
        }
        return count;
    }
}

