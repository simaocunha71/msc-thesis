        int result = 0;
        for (int i = 0; i < value.length(); i++) {
            if (value.charAt(i) >= 'A' && value.charAt(i) <= 'Z') {
                result += 1;
            }
        }
        return result;
    }
}

