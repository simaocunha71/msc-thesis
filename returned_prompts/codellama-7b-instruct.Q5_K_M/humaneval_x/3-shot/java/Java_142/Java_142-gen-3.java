        int sum = 0;
        for (int i = 0; i < lst.size(); i++) {
            if (i % 3 == 0 && i % 4 != 0) {
                sum += Math.pow(lst.get(i), 3);
            } else if (i % 4 == 0 && i % 3 != 0) {
                sum += Math.pow(lst.get(i), 2);
            }
        }
        return sum;
    }
}

