        List<String> result = new ArrayList<>();
        for (String word : lst) {
            if (word.length() % 2 == 0) {
                result.add(word);
            }
        }
        Collections.sort(result, (a, b) -> {
            if (a.length() != b.length()) {
                return Integer.compare(a.length(), b.length());
            } else {
                return a.compareTo(b);
            }
        });
        return result;
    }
}


