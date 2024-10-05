        Collections.sort(l);
        int len = l.size();

        if (len % 2 == 0) {
            return (l.get(len / 2) + l.get(len / 2 - 1)) / 2.0;
        } else {
            return l.get(len / 2);
        }
    }
}

