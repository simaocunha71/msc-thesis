        Collections.sort(l);
        if (l.size() % 2 == 1) return l.get(l.size() / 2);
        else return (l.get(l.size() / 2 - 1) + l.get(l.size() / 2)) / 2.0;
    }
}

