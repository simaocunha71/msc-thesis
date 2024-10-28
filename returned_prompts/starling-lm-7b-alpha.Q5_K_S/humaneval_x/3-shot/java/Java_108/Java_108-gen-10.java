        int result = 0;
        for (int number : arr) {
            int sum = 0;
            int sign = 1;
            while (number != 0) {
                sum += Math.abs(number % 10) * sign;
                number /= 10;
                sign *= -1;
            }
            if (sum > 0) result += 1;
        }
        return result;
    }
}

