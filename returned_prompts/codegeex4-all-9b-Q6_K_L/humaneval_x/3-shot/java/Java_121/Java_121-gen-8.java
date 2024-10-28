        int sum = 0;
        for (int i = 0; i < lst.size(); i++) {
            if (lst.get(i) % 2 != 0 && i % 2 == 0) {
                sum += lst.get(i);
            }
        }
        return sum;
    }
}

