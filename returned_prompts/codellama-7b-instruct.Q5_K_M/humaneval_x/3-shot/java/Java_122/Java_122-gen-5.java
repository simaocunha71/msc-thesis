        int sum = 0;
        for (int i = 0; i < Math.min(k, arr.size()); i++) {
            int current_digit = arr.get(i);
            sum += current_digit;
        }
        return sum;
    }
}

