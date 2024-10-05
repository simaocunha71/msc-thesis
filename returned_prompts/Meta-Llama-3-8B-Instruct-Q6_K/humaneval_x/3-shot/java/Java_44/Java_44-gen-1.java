        String result = "";
        while (x > 0) {
            int remainder = x % base;
            if (remainder > 9) {
                result = (char) (remainder + 55) + result;
            } else {
                result = remainder + "";
            }
            x /= base;
        }
        return result;
    }
}

