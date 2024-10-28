        Collections.sort(l);
        int size = l.size();
        if (size % 2 == 1) {
            return l.get(size / 2);
        } else {
            int mid1 = l.get(size / 2 - 1);
            int mid2 = l.get(size / 2);
            return (mid1 + mid2) / 2.0;
        }
    }
}

