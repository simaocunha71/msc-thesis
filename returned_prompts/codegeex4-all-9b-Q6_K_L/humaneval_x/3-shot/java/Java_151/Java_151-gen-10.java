        int sum = 0;

        for (Object number : lst) {
            if (number instanceof Integer && (Integer) number % 2 != 0) {
                sum += (Integer) number * (Integer) number;
            }
        }
        return sum;
    }
}

