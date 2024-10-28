        Collections.sort(l);
        if (l.size() % 2 == 1) {
            return l.get(l.size() / 2);
        } else {
            int mid1 = l.get(l.size() / 2);
            int mid2 = l.get(l.size() / 2 - 1);
            return (mid1 + mid2) / 2.0;
        }
    }
}

