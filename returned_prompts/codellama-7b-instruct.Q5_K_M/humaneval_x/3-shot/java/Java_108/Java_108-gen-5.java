        int count = 0;
        for (int e : arr) {
            int sum = 0;
            while (e != 0) {
                sum += e % 10;
                e /= 10;
            }
            if (sum > 0) count += 1;
        }
        return count;
    }
}

