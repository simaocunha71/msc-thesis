        lst.removeIf(str -> str.length() % 2 != 0);
        Collections.sort(lst, (a, b) -> a.length() - b.length());
        return lst;

    }
}

