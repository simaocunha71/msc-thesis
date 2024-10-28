        Collections.sort(l);
        int m = l.size();
        if (m % 2 == 0) return (l.get(m / 2) + l.get(m / 2 - 1)) / 2.0;
        else return l.get(m / 2);
    }
}

