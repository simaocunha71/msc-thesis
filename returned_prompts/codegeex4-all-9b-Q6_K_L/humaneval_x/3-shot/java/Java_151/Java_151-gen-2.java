        int sum = 0;
        for (Object item : lst) {
            if (item instanceof Integer) {
                int number = (int) item;
                if (number % 2 == 1) {
                    sum += number * number;
                }
            }
        }
        return sum;
    }
}

