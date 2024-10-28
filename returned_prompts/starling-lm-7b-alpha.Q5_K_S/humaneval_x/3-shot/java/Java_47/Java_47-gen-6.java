        Collections.sort(l);
        int length = l.size();

        return (length % 2 == 0) ? (l.get(length / 2) + l.get(length / 2 - 1)) / 2.0 : l.get(length / 2);
    }
}

