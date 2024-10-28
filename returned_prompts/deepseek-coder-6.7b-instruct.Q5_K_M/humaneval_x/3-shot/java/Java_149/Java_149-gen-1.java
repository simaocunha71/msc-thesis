        lst.removeIf(s -> s.length() % 2 != 0);
        Collections.sort(lst, Comparator.comparing(String::length).thenComparing(String::compareTo));
        return lst;
    }
}

