        Collections.sort(l);
        return l.size() % 2 != 0 ? (double) l.get(l.size() / 2) : (double) (l.get(l.size() / 2 - 1) + l.get(l.size() / 2)) / 2.0;
    }
}

