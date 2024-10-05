        lst.removeIf(s -> s.length() % 2 != 0);
        Collections.sort(lst);
        return lst;
    }
}

