        int count = 0;

        for (int number : arr) {
            int sum = 0;
            boolean isNegative = false;

            if (number < 0) {
                isNegative = true;
                number *= -1;
            }

            while (number > 0) {
                sum += number % 10;
                number /= 10;
            }

            if (isNegative) {
                sum *= -1;
            }

            if (sum > 0) {
                count += 1;
            }
        }

        return count;
    }
}

