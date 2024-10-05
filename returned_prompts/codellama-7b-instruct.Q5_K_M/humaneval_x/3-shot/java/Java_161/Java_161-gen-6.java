        char[] array = s.toCharArray();
        String result = "";
        for (int i = 0; i < array.length; i++) {
            if (Character.isLetter(array[i])) {
                if (Character.isLowerCase(array[i])) {
                    result += Character.toUpperCase(array[i]);
                } else {
                    result += Character.toLowerCase(array[i]);
                }
            } else {
                result += array[i];
            }
        }
        return result;
    }
}

