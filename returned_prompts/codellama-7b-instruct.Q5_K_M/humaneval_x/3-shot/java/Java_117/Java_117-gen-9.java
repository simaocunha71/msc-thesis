        List<String> result = new ArrayList<>();
        String[] words = s.split("\\s+");

        for (String word : words) {
            char[] chars = word.toCharArray();
            int count = 0;
            for (char c : chars) {
                if (!isVowel(c)) count++;
            }
            if (count == n) result.add(word);
        }
        return result;
    }

    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}

