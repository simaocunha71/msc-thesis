        int result = 0;
        for (int i = 0; i < k; i++) {
            int current_number = arr.get(i);
            if (current_number > 9 && i + 1 < k) {
                result += current_number % 10;
            } else {
                result += current_number;
            }
        }
        return result;
    }
}

