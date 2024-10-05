        int result = 0;
        for (int i = 0; i < arr.size(); i++) {
            int num = Math.abs(arr.get(i));
            int sum = 0;
            while (num > 0) {
                sum += num % 10;
                num /= 10;
            }
            if (sum > 0) result += 1;
        }
        return result;
    }
}

