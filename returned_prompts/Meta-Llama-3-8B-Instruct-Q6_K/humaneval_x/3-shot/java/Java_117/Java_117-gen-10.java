        List<String> result = new ArrayList<>();
        String[] words = s.split(" ");
        for (String word : words) {
            int count = 0;
            for (char c : word.toLowerCase().toCharArray()) {
                if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' && c != ' ') {
                    count++;
                }
            }
            if (count == n) {
                result.add(word);
            }
        }
        return result;
    }
}

