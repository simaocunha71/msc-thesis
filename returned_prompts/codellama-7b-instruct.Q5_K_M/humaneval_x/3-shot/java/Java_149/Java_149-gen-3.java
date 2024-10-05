        lst.removeIf(s -> s.length() % 2 == 1);
        lst.sort(Comparator.comparingInt(String::length).thenComparing(String::compareTo));
        return lst;
    }
}

