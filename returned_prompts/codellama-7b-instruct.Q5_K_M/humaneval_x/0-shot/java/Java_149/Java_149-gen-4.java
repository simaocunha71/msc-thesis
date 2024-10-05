        // your code goes here
        lst.sort(Comparator.comparing(String::length));
        lst.removeIf(s -> s.length() % 2 == 1);
        lst.sort(String::compareTo);
        return lst;
    }
}