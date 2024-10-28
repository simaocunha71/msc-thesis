        int length = string.length();
        if (length < 2) return false;
        for (int i = 2; i < length; i++) {
            if (length % i == 0) return false;
        }
        return true;
     }
}

