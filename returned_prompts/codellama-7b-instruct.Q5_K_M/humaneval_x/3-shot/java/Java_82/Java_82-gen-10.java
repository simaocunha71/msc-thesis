        int length = string.length();
        for (int i = 2; i <= length; i++) {
            if (length % i == 0) {
                if (i == length) return true;
                else continue;
            }
        }
        return false;
    }
}

