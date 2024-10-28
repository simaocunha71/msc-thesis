        String result = "";
        String binary = Integer.toBinaryString(N);
        int sum = 0;

        for (int i = 0; i < binary.length(); i++) {
            if (binary.charAt(i) == '1') sum += 1;
        }
        return Integer.toString(sum);
    }
}

