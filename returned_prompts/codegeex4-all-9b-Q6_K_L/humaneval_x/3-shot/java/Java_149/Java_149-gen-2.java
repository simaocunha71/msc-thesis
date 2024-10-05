        lst.removeIf(s -> s.length() % 2 != 0);
        Collections.sort(lst, Comparator.comparingInt(String::length).thenComparing(String::compareTo));
        return lst;
    }
}

