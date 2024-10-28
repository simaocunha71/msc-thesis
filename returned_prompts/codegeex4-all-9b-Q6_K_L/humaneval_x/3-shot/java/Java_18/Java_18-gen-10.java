        int count = 0;
        int position = 0;
        while ((position = string.indexOf(substring, position)) != -1) {
            count += 1;
            position += 1;
        }
        return count;
    }
}

