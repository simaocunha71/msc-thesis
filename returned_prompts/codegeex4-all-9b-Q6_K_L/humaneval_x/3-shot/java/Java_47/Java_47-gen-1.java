        Collections.sort(l);
        if (l.size() % 2 == 0) {
            return (l.get(l.size() / 2) + l.get(l.size() / 2 - 1)) / 2.0;
        }
        return l.get(l.size() / 2);
    }
}

