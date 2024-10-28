        List<String> result = new ArrayList<>();
        String[] words = s.split(" ");

        for (String word : words) {
            int vowels = 0;
            for (char c : word.toCharArray()) {
                if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') continue;
                vowels += 1;
            }
            if (vowels == n) result.add(word);
        }
        return result;
    }
}

