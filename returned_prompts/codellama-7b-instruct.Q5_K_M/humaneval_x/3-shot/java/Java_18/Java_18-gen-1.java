        int count = 0;
        int index = 0;
        while (true) {
            int new_index = string.indexOf(substring, index);

            if (new_index == -1) break;

            count += 1;
            index = new_index + substring.length();
        }
        return count;

    }
}

