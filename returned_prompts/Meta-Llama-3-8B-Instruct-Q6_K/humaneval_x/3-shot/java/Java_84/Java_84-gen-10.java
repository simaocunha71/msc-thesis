        int sum = 0;
        String bin = Integer.toBinaryString(N);
        for (int i = 0; i < bin.length(); i++) {
            sum += bin.charAt(i) - '0';
        }
        return Integer.toBinaryString(sum);
    }
}

