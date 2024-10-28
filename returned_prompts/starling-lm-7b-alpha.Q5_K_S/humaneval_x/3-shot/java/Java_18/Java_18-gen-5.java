        int result = 0;
        for (int start_index = 0; start_index < string.length(); start_index++) {
            int index = start_index;
            while (index < string.length() && string.substring(index, index + substring.length()).equals(substring)) {
                index += 1;
            }
            result += (index - start_index);
        }
        return result;
    }
}

