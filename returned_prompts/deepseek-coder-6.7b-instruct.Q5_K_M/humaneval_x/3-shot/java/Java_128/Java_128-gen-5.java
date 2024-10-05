        if (arr.size() == 0) {
            return Optional.empty();
        }

        int result = 0;
        int sign = 1;

        for (int num : arr) {
            if (num == 0) {
                return Optional.of(0);
            }

            if (num < 0) {
                sign *= -1;
                result += Math.abs(num);
            } else {
                result += num;
            }
        }

        return Optional.of(result * sign);
     }
}

