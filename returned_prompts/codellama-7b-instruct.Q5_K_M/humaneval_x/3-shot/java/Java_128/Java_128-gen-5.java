        if (arr.isEmpty()) {
            return Optional.empty();
        } else {
            int product = 1;
            int sum = 0;

            for (int i = 0; i < arr.size(); i++) {
                if (arr.get(i) == 0) {
                    product = 0;
                } else if (arr.get(i) < 0) {
                    product = -1;
                }
                sum += Math.abs(arr.get(i)) * product;
            }
            return Optional.of(sum);
        }
    }
}

