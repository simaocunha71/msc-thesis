        int count = 0;
        int index = 0;
        while (index < string.length()) {
            index = string.indexOf(substring, index);
            if (index != -1) {
                count++;
                index++;
            } else {
                break;
            }
        }
        return count;
    }
}

