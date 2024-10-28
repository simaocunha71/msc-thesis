    List<String> result = new ArrayList<>();
    for (String str : lst) {
        if (str.length() % 2 == 0) {
            result.add(str);
        }
    }
    Collections.sort(result, new Comparator<String>() {
        @Override
        public int compare(String s1, String s2) {
            if (s1.length() != s2.length()) {
                return s1.length() - s2.length();
            } else {
                return s1.compareTo(s2);
            }
        }
    });
    return result;
}
