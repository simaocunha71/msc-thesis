        int sum = 0;
        for (int i = 0; i < lst.size(); i++) {
            if (i % 3 == 0) {
                sum += Math.pow(lst.get(i), 2);
            }
            if (i % 4 == 0 && i % 3 != 0) {
                sum += Math.pow(lst.get(i), 3);
            }
        }
        return sum;
    }
}

