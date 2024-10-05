        int sum = 0;
        for (int i = 0; i < k && i < arr.size(); i++) {
            int n = arr.get(i);
            if (String.valueOf(n).length() <= 2) {
                sum += n;
            }
        }
        return sum;
    }
}

