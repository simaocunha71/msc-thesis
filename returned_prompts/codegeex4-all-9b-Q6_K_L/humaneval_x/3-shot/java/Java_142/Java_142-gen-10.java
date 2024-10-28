        int sum = 0;

        for (int i = 0; i < lst.size(); i++) {
            if (i % 3 == 0) {
                sum += lst.get(i) * lst.get(i);
            } else if (i % 4 == 0) {
                sum += lst.get(i) * lst.get(i) * lst.get(i);
            } else {
                sum += lst.get(i);
            }
        }
        return sum;
    }
}

