        StringBuilder result = new StringBuilder();
        while (x > 0) {
            x = x % base;
            if (x > 9) {
                result.insert(0, (char) (x + 55));
            } else {
                result.insert(0, x);
            }
            x = x / base;
        }
        return result.toString();
    }
}

