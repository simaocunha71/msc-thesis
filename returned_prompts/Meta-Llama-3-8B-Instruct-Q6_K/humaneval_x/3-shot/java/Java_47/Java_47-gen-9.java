        Collections.sort(l);
        int size = l.size();
        if (size % 2 == 0) {
            double mid1 = l.get(size / 2 - 1);
            double mid2 = l.get(size / 2);
            return (mid1 + mid2) / 2.0;
        } else {
            return (double) l.get(size / 2);
        }
    }
}

