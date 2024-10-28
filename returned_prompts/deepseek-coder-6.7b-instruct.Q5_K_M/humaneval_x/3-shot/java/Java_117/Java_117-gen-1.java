        String[] words = s.split(" ");
        List<String> result = new ArrayList<>();
        Set<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));

        for (String word : words) {
            int count = 0;
            for (char c : word.toCharArray()) {
                if (!vowels.contains(c)) {
                    count++;
                    if (count == n) {
                        result.add(word);
                        break;
                    }
                }
            }
        }
        return result;
    }
}

