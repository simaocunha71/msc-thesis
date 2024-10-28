        int n = l.size();
        Collections.sort(l);

        if (n % 2 == 0) {
            return (l.get(n / 2 - 1) + l.get(n / 2)) / 2.0;
        } else {
            return l.get(n / 2);
        }
    }
}

