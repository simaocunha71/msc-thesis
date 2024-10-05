        List<String> result = new ArrayList<>();
        Set<String> consonants = new HashSet<>(Arrays.asList("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"));

        for (String word : s.split(" ")) {
            int count = 0;
            for (char c : word.toCharArray()) {
                if (!consonants.contains(String.valueOf(c).toLowerCase())) {
                    count += 1;
                }
                if (count == n) {
                    result.add(word);
                }
                if (count > n) {
                    break;
                }
            }
        }
        return result;
    }
}

