        List<String> result = new ArrayList<>();
        for (String s : lst) {
            if (s.length() % 2 == 0) result.add(s);
        }
        Collections.sort(result, (o1, o2) -> {
            if (o1.length() != o2.length()) return Integer.compare(o1.length(), o2.length());
            return o1.compareTo(o2);
        });
        return result;
    }
}

