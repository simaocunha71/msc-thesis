        List<String> result = new ArrayList<>();
        for (String s : lst) {
            if (s.length() % 2 == 0) {
                result.add(s);
            }
        }
        Collections.sort(result, (a, b) -> a.length() != b.length() ? a.length() - b.length() : a.compareTo(b));
        return result;
    }
}

