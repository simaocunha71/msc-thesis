        if (l.size() == 0) return 0.0;
        Collections.sort(l);
        if (l.size() % 2 == 0) return (double) (l.get(l.size() / 2) + l.get(l.size() / 2 - 1)) / 2;
        else return l.get(l.size() / 2);
    }
}

