        int length = string.length();
        if (length == 1) return true;

        for (int i = 2; i <= length / 2; i++) {
            if (length % i == 0) return false;
        }
        return true;
}