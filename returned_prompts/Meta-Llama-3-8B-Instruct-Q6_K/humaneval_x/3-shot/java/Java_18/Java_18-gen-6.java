        int count = 0;
        int pos = 0;

        while ((pos = string.indexOf(substring, pos)) != -1) {
            count++;
            pos += substring.length();
        }

        return count;
    }
}

