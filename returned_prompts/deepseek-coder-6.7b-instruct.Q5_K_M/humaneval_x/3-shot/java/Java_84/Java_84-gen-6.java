        int sum = 0;
        StringBuilder binary = new StringBuilder();

        while (N > 0) {
            sum += N % 2;
            N /= 2;
        }

        while (sum > 0) {
            binary.insert(0, sum % 2);
            sum /= 2;
        }

        return binary.toString();
     }
}

