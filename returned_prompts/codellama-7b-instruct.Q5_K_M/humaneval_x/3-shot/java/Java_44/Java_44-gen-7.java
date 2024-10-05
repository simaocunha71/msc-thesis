        String result = "";
        while (x != 0) {
            result = (x % base) + result;
            x /= base;
        }
        return result;
    }
}

