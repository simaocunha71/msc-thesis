        Collections.sort(l);
        int size = l.size();
        if (size % 2 == 0) {
            int mid1 = l.get(size / 2 - 1);
            int mid2 = l.get(size / 2);
            return (double) (mid1 + mid2) / 2;
        } else {
            return (double) l.get(size / 2);
        }
    }
}

