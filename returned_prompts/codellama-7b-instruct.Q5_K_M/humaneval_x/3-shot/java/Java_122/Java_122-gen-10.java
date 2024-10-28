        int sum = 0;
        int start = 0;
        int end = Math.min(k, arr.size());

        for (int i = start; i < end; i++) {
            sum += arr.get(i);
        }
        return sum;
    }
}

