        String result = "";
        while (x != 0) {
            result = String.valueOf(x % base) + result;
            x /= base;
        }
        return result;
    }
}

