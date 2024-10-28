        // Base conversion logic goes here
        StringBuilder sb = new StringBuilder();
        while (x > 0) {
            int remainder = x % base;
            if (remainder < 10) {
                sb.insert(0, (char) ('0' + remainder));
            } else {
                sb.insert(0, (char) ('A' + remainder - 10));
            }
            x = x / base;
        }
        return sb.toString();
    }
}
