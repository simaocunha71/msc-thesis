        StringBuilder result = new StringBuilder();
        while (x > 0) {
            int remainder = x % base;
            if (remainder > 9) {
                result.insert(0, (char) (remainder + 55)); // ASCII value of 'A' is 65
            } else {
                result.insert(0, remainder);
            }
            x /= base;
        }
        return result.toString();
    }
}

