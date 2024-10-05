        List<String> result = new ArrayList<>();
        for (String s : lst) {
            if (s.length() % 2 == 0) result.add(s);
        }
        result.sort((x, y) -> x.length() == y.length() ? x.compareTo(y) : x.length() - y.length());
        return result;
    }
}

