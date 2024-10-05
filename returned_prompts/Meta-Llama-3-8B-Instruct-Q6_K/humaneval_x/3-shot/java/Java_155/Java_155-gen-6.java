        int even = 0, odd = 0;
        String s = String.valueOf(Math.abs(num));
        for (char c : s.toCharArray()) {
            if (Character.getNumericValue(c) % 2 == 0) {
                even++;
            } else {
                odd++;
            }
        }
        return Arrays.asList(even, odd);
    }
}

