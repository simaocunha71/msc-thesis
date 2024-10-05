        int[] arr = new int[10];
        int sum = 0;
        int product = 0;
        while (n > 0) {
            int num = n % 10;
            if (num % 2 == 1) {
                sum = sum + num;
            }
            n /= 10;
        }
        if (sum == 0) {
            return 0;
        }
        while (sum > 0) {
            int num = sum % 10;
            if (num % 2 == 1) {
                product = product * num;
            }
            sum /= 10;
        }
        return product;
    }
}

