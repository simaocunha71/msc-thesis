        int result = 0;
        for (int i : arr) {
            int sum = 0;
            while (i != 0) {
                sum += i % 10;
                i /= 10;
            }
            if (sum > 0) result += 1;
        }
        return result;
    }
}

