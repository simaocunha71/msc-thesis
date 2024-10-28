        int digit = 0;
        for (char c : value.toCharArray()) {
            if (c >= '0' && c <= '9') {
                digit += 1;
            }
        }
        return digit;
    }
}


```