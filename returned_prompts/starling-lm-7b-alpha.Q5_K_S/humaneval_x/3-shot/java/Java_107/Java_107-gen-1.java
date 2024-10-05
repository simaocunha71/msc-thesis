        char[] char_array = number_str.toCharArray();
        int left = 0;
        int right = number_str.length() - 1;
        while (left < right) {
            char temp = char_array[left];
            char_array[left] = char_array[right];
            char_array[right] = temp;
            left += 1;
            right -= 1;
        }
        return new String(char_array);
    }
}

