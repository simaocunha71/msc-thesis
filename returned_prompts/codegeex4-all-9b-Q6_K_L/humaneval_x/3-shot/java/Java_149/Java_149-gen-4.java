        lst.removeIf(s -> s.length() % 2 == 1);
        Collections.sort(lst);
        return lst;
    }
}

