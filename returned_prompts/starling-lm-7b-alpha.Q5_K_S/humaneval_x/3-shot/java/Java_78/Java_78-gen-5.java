        int result = 0;
        for (char c : num.toCharArray()) {
            if (c >= '0' && c <= '9') {
                result += isPrime(c - '0');
            } else if (c >= 'A' && c <= 'F') {
                result += isPrime(c - 'A' + 10);
            }
        }
        return result;
    }
}

