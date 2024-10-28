        String result = "";
        while (x > 0) {
            int remainder = x % base;
            result = remainder + result;
            x /= base;
        }
        return result;
    }
}

