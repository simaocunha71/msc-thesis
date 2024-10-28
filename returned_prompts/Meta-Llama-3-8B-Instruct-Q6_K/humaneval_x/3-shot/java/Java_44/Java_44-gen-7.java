        StringBuilder result = new StringBuilder();
        while (x > 0) {
            x = x % base;
            if (x > 9) {
                result.append((char) (x + 55));
            } else {
                result.append(x);
            }
            x /= base;
        }
        return result.reverse().toString();
    }
}

