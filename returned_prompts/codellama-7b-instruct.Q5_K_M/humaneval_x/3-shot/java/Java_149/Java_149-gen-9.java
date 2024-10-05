        lst.removeIf(s -> s.length() % 2 != 0);
        lst.sort((s1, s2) -> {
            if (s1.length() < s2.length()) return -1;
            if (s1.length() > s2.length()) return 1;
            return s1.compareTo(s2);
        });
        return lst;
    }
}

