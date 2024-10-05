        int length = string.length();
        if (length <= 1) return false;
        if (length == 2) return true;
        for (int i = 3; i * i <= length; i += 2) {
            if (length % i == 0) return false;
        }
        return true;
    }
}