        int sum = 0;
        int len = lst.size();
        for (int i = 0; i < len; i++) {
            int num = lst.get(i);
            if (i % 2 == 0 && num % 2 != 0) {
                sum += num;
            }
        }
        return sum;
    }
}
