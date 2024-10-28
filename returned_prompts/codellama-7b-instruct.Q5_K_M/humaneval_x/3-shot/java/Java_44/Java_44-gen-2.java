        String result = "";
        while (x > 0) {
            int remainder = x % base;
            result = String.valueOf(remainder) + result;
            x /= base;
        }
        return result;
    }
}

