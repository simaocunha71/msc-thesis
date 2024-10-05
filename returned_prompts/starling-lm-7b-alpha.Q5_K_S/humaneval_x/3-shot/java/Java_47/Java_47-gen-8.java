        Collections.sort(l);
        int n = l.size();
        if (n % 2 == 0) {
            int i = n / 2;
            return (l.get(i) + l.get(i - 1)) / 2.0;
        } else {
            return l.get(n / 2);
        }
    }
}

