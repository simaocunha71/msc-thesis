        lst.removeIf(x -> x.length() % 2 == 1);
        Collections.sort(lst, (a, b) -> a.length() == b.length() ? a.compareTo(b) : a.length() - b.length());
        return lst;
    }
}

