        int sum = 0;
        for (int i = 0; i < k; i++) {
            if (arr.get(i) >= 10 && arr.get(i) <= 99) {
                sum += arr.get(i);
            }
        }
        return sum;
     }
}

