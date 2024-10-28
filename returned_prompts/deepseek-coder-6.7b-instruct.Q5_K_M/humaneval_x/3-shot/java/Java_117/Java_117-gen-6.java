        String[] words = s.split(" ");
        List<String> result = new ArrayList<>();

        for (String word : words) {
            int count = 0;
            for (char c : word.toCharArray()) {
                if (isConsonant(c)) count++;
            }
            if (count == n) result.add(word);
        }
        return result;
    }

    private boolean isConsonant(char c) {
        c = Character.toLowerCase(c);
        return c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' && c >= 'a' && c <= 'z';
    }
}

