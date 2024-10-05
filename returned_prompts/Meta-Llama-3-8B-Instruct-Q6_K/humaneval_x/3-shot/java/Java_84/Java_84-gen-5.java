        int sum = 0;
        String bin = Integer.toBinaryString(N);
        for (char c : bin.toCharArray()) {
            if (c == '1') sum += 1;
        }
        return Integer.toBinaryString(sum);
    }
}

