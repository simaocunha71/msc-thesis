        lst.removeIf(str -> str.length() % 2 == 1);
        lst.sort((s1, s2) -> {
            if (s1.length() == s2.length()) {
                return s1.compareTo(s2);
            }
            return Integer.compare(s1.length(), s2.length());
        });
        return lst;
    }
}

