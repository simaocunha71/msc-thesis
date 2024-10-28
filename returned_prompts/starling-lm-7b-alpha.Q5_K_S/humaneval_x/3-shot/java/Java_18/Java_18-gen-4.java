        int result = 0;
        int current_start = 0;
        while (true) {
            int start_index = string.indexOf(substring, current_start);
            if (start_index == -1) break;
            result += 1;
            current_start = start_index + 1;
        }
        return result;
    }
}

