        StringBuilder result = new StringBuilder();
        while (x > 0) {
            int remainder = x % base;
            result.insert(0, remainder);
            x /= base;
        }
        return result.toString();
    }
}

