        List<String> result = new ArrayList<>();

        for (String s : lst) {
            if (s.length() % 2 == 0) result.add(s);
        }

        result.sort((String a, String b) -> {
            if (a.length() == b.length()) {
                return a.compareTo(b);
            }
            return a.length() - b.length();
        });

        return result;
    }
}

