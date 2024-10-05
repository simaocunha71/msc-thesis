        int length = string.length();
        if (length  % 2 == 0) return false;
        for  (int i = 3; i * i <= length; i += 2) {
            if (length % i == 0) return false;
        }
        return length > 1;
     }
}

