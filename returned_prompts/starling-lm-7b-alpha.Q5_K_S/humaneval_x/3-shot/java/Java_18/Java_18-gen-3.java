        int result = 0;
        for (int i = 0; i < string.length(); i++) {
            int index = i;
            for (; index < string.length(); index++) {
                if (string.charAt(index) == substring.charAt(index - i)) {
                    if (index == substring.length() - 1) {
                        result += 1;
                        i = index + 1;
                        break;
                    }
                } else {
                    index = i;
                    break;
                }
            }
        }
        return result;
    }
}

