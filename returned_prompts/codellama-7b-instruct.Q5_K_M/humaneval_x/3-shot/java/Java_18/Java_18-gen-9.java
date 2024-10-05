        int count = 0;
        int pos = 0;
        while (pos >= 0) {
            pos = string.indexOf(substring, pos);
            if (pos >= 0) {
                count += 1;
                pos += substring.length();
            }
        }
        return count;
    }
}

