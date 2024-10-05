        String[] digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"};
        StringBuilder result = new StringBuilder();

        while (x > 0) {
            int remainder = x % base;
            result.insert(0, digits[remainder]);
            x /= base;
        }
        return result.toString();
    }
}

