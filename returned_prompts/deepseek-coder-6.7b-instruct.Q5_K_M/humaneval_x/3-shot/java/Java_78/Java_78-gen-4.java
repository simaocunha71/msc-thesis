        Set<Character> primeHexChars = new HashSet<>(Arrays.asList('2', '3', '5', '7', 'B', 'D'));
        int count = 0;
        for (char ch : num.toCharArray()) {
            if (primeHexChars.contains(ch)) {
                count++;
            }
        }
        return count;
    }
}

