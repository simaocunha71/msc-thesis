        int count = 0;
        for (int num : arr) {
            int sum = 0;
            if (num < 0) {
                for (char c : String.valueOf(num).substring(1).toCharArray()) {
                    sum += Character.getNumericValue(c);
                }
            } else {
                for (char c : String.valueOf(num).toCharArray()) {
                    sum += Character.getNumericValue(c);
                }
            }
            if (sum > 0) {
                count++;
            }
        }
        return count;
    }
}

