        Set<Character> primeHex = new HashSet<>(Arrays.asList('2', '3', '5', '7', 'B', 'D'));
        int count = 0;

        for(char c : num.toCharArray()) {
            if(primeHex.contains(c)) {
                count++;
            }
        }
        return count;
    }
}

