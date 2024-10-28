        Collections.sort(l);
        int length = l.size();
        if (length % 2 == 0) {
            return (l.get(length / 2 - 1) + l.get(length / 2)) / 2.0;
        } else {
            return l.get(length / 2);
        }
    }
}

