        String result = "";

        for (int i = 0; i < s.length(); i++) {
            int current_index = s.charAt(i) - 'a';
            int new_index = (current_index + 2) % 26;
            result += (char) ('a' + new_index);
        }
        return result;
    }
}

