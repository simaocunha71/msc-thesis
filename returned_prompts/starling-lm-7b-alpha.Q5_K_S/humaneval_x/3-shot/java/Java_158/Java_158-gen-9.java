        int max_count = 0;
        String result = "";
        for (String word : words) {
            int count = 0;
            for (char c : word.toCharArray()) {
                if (!word.contains(String.valueOf(c))) {
                    count += 1;
                }
            }
            if (count > max_count) {
                result = word;
                max_count = count;
            } else if (count == max_count && word.compareTo(result) < 0) {
                result = word;
            }
        }
        return result;
    }
}

