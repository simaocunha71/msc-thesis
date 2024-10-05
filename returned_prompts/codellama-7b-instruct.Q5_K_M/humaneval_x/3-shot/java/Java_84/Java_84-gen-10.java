        String binary_string = "";
        int remainder;

        while (N > 0) {
            remainder = N % 2;
            binary_string = remainder + binary_string;
            N /= 2;
        }
        return binary_string;
    }
}

