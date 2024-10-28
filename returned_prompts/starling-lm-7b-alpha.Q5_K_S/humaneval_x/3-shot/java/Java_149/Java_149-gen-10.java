        List<String> result = new ArrayList<>();
        for (String str : lst) {
            if (str.length() % 2 == 0) {
                result.add(str);
            }
        }
        Collections.sort(result, (s1, s2) -> {
            if (s1.length() == s2.length()) {
                return s1.compareTo(s2);
            }
            return s1.length() - s2.length();
        });
        return result;
    }
}

