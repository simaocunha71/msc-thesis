    public int howManyTimes(String string, String substring) {
        if (substring.isEmpty()) {
            return 0;
        }

        int count = 0;
        int index = 0;

        while ((index = string.indexOf(substring, index)) != -1) {
            count++;
            index += substring.length();
        }

        return count;
    }A

