        if (substring.isEmpty()) return 0;
        int count = 0;
        int index = string.indexOf(substring);

        while (index != -1) {
            count++;
            index = string.indexOf(substring, index + 1);
        }
        return count;
    }
}

