        Collections.sort(l);
        int size = l.size();
        double result = 0.0;

        if (size % 2 == 1) {
            result = l.get(size / 2);
        } else {
            result = (l.get(size / 2) + l.get(size / 2 - 1)) / 2.0;
        }
        return result;
    }
}

