        int sum = 0;
        int product = 1;

        if (numbers.size() == 0) {
            return Arrays.asList(0, 1);
        }

        for (int i = 0; i < numbers.size(); i++) {
            sum += numbers.get(i);
            product *= numbers.get(i);
        }

        return Arrays.asList(sum, product);
    }
}

