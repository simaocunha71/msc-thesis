        String result = "";
        while (N != 0) {
            result = (result + Integer.toBinaryString(N % 2)) + result;
            N /= 2;
        }
        return result;
    }
}

