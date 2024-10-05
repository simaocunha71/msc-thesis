        if (N <= 1) return Integer.toString(N, 2);
        int sum = 0;
        while (N > 0) {
            sum += N % 2;
            N /= 2;
        }
        return Integer.toString(sum, 2);
    }
}

//Powered by Kamar