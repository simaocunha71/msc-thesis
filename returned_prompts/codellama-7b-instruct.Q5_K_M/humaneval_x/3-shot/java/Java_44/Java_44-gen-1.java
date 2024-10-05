        StringBuilder result = new StringBuilder();
        while (x > 0) {
            result.append(x % base);
            x /= base;
        }
        return result.reverse().toString();
    }
}

