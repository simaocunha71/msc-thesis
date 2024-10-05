        char[] array = string.toCharArray();
        for (int i = 0; i < array.length; i++) {
            char c = array[i];
            if (c >= 'a' && c <= 'z') {
                array[i] = (char) (c - 32);
            } else if (c >= 'A' && c <= 'Z') {
                array[i] = (char) (c + 32);
            }
        }
        return String.valueOf(array);
    }
}

