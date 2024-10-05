        lst.removeIf(e -> e.length() % 2 != 0);
        Collections.sort(lst);
        return lst;
    }
}

