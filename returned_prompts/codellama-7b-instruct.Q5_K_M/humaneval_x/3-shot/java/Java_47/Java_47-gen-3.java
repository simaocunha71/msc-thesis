        Collections.sort(l);
        int n = l.size();
        if (n % 2 == 1) {
            return l.get(n / 2);
        } else {
            return (l.get(n / 2 - 1) + l.get(n / 2)) / 2.0;
        }
    }
}

