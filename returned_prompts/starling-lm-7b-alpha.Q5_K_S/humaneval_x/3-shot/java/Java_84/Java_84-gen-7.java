        String result = "";
        while (N != 0) {
            result = (N % 2) + result;
            N = N / 2;
        }
        return result;
    }
}

