        if (arr.size() == 0) return Optional.empty();

        long result = 0;
        long product = 1;
        for (int i = 0; i < arr.size(); i++) {
            int number = arr.get(i);
            if (number == 0) {
                result = 0;
                product = 1;
                continue;
            }

            if (number > 0) {
                result += number;
            } else {
                result -= number;
            }

            product *= number;
        }
        return Optional.of((int) Math.abs(result));
    }
}

