        lst.removeIf(x -> x.length() % 2 == 1);
        lst.sort((x, y) -> x.length() != y.length() ? x.length() - y.length() : x.compareTo(y));
        return lst;
    }
}

