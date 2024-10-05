        int sum = 0;
        for (int i = 0; i < k; i++) {
            int num = arr.get(i);
            if (String.valueOf(num).length() <= 2) {
                sum += num;
            }
        }
        return sum;
    }
}

