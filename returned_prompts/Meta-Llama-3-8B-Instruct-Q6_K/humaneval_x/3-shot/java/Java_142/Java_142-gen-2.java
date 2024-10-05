        int sum = 0;
        for (int i = 0; i < lst.size(); i++) {
            if ((i + 1) % 3 == 0 && (i + 1) % 4 != 0) {
                sum += Math.pow(lst.get(i), 2);
            } else if ((i + 1) % 4 == 0 && (i + 1) % 3 != 0) {
                sum += Math.pow(lst.get(i), 3);
            } else {
                sum += lst.get(i);
            }
        }
        return sum;
    }
}

