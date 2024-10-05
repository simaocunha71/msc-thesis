        Collections.sort(l);
        int n = l.size();
        if (n % 2 == 0) {
            return (double) (l.get(n / 2) + l.get(n / 2 - 1)) / 2;
        } else {
            return (double) l.get(n / 2);
        }
    }
}

