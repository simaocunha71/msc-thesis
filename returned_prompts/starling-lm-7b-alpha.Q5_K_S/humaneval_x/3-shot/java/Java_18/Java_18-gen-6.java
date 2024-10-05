        int count = 0;
        int index = -1;
        while (true) {
            index = string.indexOf(substring, index + 1);
            if (index == -1) break;
            count += 1;
        }
        return count;
    }
}

