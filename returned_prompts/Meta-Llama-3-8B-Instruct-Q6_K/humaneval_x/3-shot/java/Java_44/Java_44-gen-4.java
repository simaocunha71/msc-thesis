        StringBuilder sb = new StringBuilder();
        while (x > 0) {
            x = x % base;
            if (x > 9) {
                sb.insert(0, (char) (x + 55));
            } else {
                sb.insert(0, x);
            }
            x = x / base;
        }
        return sb.toString();
    }
}

