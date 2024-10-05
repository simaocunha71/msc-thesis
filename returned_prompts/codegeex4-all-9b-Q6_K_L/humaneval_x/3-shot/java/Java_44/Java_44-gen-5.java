        StringBuilder result = new StringBuilder();

        while (x >= base) {
            result.insert(0, x % base);
            x /= base;
        }
        result.insert(0, x);
        return result.toString();
    }
}

