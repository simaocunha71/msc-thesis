        String binary = "";
        while (N > 0) {
            binary = (N % 2) + binary;
            N /= 2;
        }
        return binary;
    }
}

