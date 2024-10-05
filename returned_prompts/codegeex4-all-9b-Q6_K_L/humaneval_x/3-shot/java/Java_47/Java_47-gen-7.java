        Collections.sort(l);
        int size = l.size();

        if (size % 2 == 0) {
            return ((double)l.get(size / 2 - 1) + (double)l.get(size / 2)) / 2;
        } else {
            return (double)l.get(size / 2);
        }
    }
}

