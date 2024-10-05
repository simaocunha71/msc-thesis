        StringBuilder sb = new StringBuilder();
        while (x > 0) {
            int remainder = x % base;
            sb.append(remainder < 10 ? (char) (remainder + '0') : (char) (remainder - 10 + 'A'));
            x /= base;
        }
        return sb.reverse().toString();
    }
}

