        int len = string.length();
        if (len == 0 || (len != 2 && len % 2 == 0)) return false;
        for (int i = 3; i * i <= len; i += 2) {
            if (len % i == 0) return false;
        }
        return true;
     }
}

