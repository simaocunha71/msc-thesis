        String[] words = s.split(" ");
        List<String> result = new ArrayList<>();
        String consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ";
        for (String word : words) {
            int count = 0;
            for (char c : word.toCharArray()) {
                if (consonants.contains(String.valueOf(c))) {
                    count += 1;
                }
            }
            if (count == n) {
                result.add(word);
            }
        }
        return result;
    }
}

