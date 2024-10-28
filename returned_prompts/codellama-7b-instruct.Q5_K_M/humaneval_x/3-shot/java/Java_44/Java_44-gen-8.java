        String result = "";
        while (x > 0) {
            int remainder = x % base;
            result = (remainder < 10) ? remainder + result : (char)('A' + remainder - 10) + result;
            x = x / base;
        }
        return result;
    }
}

