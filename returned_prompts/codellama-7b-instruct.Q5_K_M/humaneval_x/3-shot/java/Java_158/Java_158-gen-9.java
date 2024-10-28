        if (words.size() == 0) return "";
        int max_unique = -1;
        String result = "";

        for (String word : words) {
            if (word.length() > max_unique) {
                max_unique = word.length();
                result = word;
            }
        }
        return result;
    }
}

