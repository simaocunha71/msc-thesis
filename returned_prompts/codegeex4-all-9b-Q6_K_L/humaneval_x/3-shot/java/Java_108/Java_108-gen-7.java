        int count = 0;
        for (int number : arr) {
            int sum = 0;
            boolean negative = false;
            if (number < 0) {
                negative = true;
                number *= -1;
            }

            while (number > 0) {
                sum += number % 10;
                number /= 10;
            }

            if (negative) {
                sum *= -1;
            }

            if (sum > 0) {
                count += 1;
            }
        }
        return count;
    }
}

