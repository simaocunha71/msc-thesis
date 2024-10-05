        StringBuilder result = new StringBuilder();
        while (x > 0) {
            int digit = x % base;
            result.append(digit);
            x /= base;
        }
        return result.reverse().toString();

    }
}

