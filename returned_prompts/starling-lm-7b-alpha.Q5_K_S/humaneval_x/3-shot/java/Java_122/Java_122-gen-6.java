        int sum = 0;
        for (int i = 0; i < Math.min(k, arr.size()); i++) {
            if (arr.get(i) < 10) {
                sum += arr.get(i);
            } else if (arr.get(i) < 100) {
                sum += arr.get(i);
            }
        }
        return sum;
    }
}

