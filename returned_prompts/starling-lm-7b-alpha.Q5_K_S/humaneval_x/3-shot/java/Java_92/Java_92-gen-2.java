        if (x instanceof Integer && y instanceof Integer && z instanceof Integer) {
            int[] numbers = {(Integer) x, (Integer) y, (Integer) z};
            Arrays.sort(numbers);

            return numbers[0] + numbers[1] == numbers[2];
        }
        return false;
    }
}

