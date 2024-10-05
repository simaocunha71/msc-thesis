        List<String> result = new ArrayList<>();
        String[] words = s.split(" ");
        for (String word : words) {
            if (word.replaceAll("[aeiou]", "").length() == n) {
                result.add(word);
            }
        }
        return result;
    }
}

