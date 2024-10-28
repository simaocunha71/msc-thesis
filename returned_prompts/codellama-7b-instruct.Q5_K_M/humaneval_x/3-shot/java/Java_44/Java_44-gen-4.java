        if (x == 0) return "0";

        String result = "";
        while (x > 0) {
            result = String.valueOf(x % base) + result;
            x /= base;
        }
        return result;
    }
}

