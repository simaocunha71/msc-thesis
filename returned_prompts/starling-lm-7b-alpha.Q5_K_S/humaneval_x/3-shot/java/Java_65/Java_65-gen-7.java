        StringBuilder result = new StringBuilder();
        for (int i = 0; i < Math.abs(shift); i++) {
            result.append(x % 10);
            x /= 10;
        }
        for (int i = 0; i < x; i++) {
            result.append(x % 10);
            x /= 10;
        }
        return result.reverse().toString();
    }
}


