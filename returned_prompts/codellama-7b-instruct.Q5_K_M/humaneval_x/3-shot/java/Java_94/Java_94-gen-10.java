        int max = 0;
        int sum = 0;

        for (int i = 0; i < lst.size(); i++) {
            if (lst.get(i) > max) {
                max = lst.get(i);
            }
        }
        while (max > 0) {
            sum += max % 10;
            max /= 10;
        }
        return sum;
    }
}

