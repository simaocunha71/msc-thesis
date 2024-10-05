        int count = 0;
        int position = 0;

        while (position < string.length()) {
            position = string.indexOf(substring, position);
            if (position == -1) break;
            count += 1;
            position += 1;
        }
        return count;
    }
}

