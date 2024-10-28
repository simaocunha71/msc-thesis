        StringBuilder result = new StringBuilder();
        while (x > 0) {
            result.insert(0, x % base);
            x /= base;
        }
        return result.toString();
    }
}

