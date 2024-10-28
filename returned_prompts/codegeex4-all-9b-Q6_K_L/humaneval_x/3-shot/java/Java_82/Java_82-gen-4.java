        int length = string.length();
        for (int i = 2; i <= Math.sqrt(length); i++) {
            if (length % i == 0) return false;
        }
        return true;
    }
}

