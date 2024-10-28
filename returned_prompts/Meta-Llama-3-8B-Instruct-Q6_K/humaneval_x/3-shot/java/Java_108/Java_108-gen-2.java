        int count = 0;
        for (int num : arr) {
            int sum = 0;
            String str = String.valueOf(Math.abs(num));
            for (char c : str.toCharArray()) {
                sum += Integer.parseInt(String.valueOf(c)) - '0';
            }
            if (sum > 0) {
                count++;
            }
        }
        return count;
    }
}

