        Collections.sort(l);
        int length = l.size();
        if (length % 2 == 1) {
            return (double)l.get(length / 2);
        } else {
            return (double)(l.get(length / 2) + l.get(length / 2 - 1)) / 2;
        }
    }
}

