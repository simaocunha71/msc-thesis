        lst.removeIf(str -> str.length() % 2 == 1);
        lst.sort((a, b) -> {
            if (a.length() != b.length()) {
                return a.length() - b.length();
            } else {
                return a.compareTo(b);
            }
        });
        return lst;
    }
}

