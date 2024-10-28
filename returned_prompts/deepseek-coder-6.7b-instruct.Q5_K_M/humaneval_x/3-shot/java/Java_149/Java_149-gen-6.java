        lst.removeIf(s -> (s.length() % 2) != 0);
        lst.sort(Comparator.comparing(String::length).thenComparing(String::compareTo));
        return lst;
     }
}

