        for (int i=1; i<l.size(); i++) {
            if (l.get(i) > l.get(i-1)) {
                l.set(i-1, l.get(i));
            }
        }
        return l.get(l.size()-1);
    }
}
