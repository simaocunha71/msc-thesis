        Collections.sort(l);
        if (l.size() % 2 == 1) {
            return l.get(l.size() / 2);
        } else {
            int i = l.size() / 2;
            return (l.get(i) + l.get(i - 1)) / 2.0;
        }
    }
}

