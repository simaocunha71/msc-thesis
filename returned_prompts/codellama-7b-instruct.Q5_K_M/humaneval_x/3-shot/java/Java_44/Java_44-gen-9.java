        if (x == 0) return "0";
        int current_base = 1;
        String result = "";

        while (current_base <= x) {
            current_base *= base;
        }

        while (current_base > 0) {
            int digit = (int)(x / current_base);
            result += (char)(digit + '0');
            x %= current_base;
            current_base /= base;
        }
        return result;
    }
}
