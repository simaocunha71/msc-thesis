        int length = string.length();
        if (length < 2) return false;
        if (length == 2 || length == 3) return true;
        if (length % 2 == 0 || length % 3 == 0) return false;
        for (int i = 5; i * i <= length; i += 6) {
            if (length % i == 0 || length % (i + 2) == 0) return false;
        }
        return true;
    }
}

