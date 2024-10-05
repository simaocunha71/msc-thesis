        int count = 0;
        for (int num : arr) {
            int sum = 0;
            for (char c : String.valueOf(Math.abs(num)).toCharArray()) {
                sum += Integer.parseInt(String.valueOf(c));
            }
            if (sum > 0) count++;
        }
        return count;
    }
}

