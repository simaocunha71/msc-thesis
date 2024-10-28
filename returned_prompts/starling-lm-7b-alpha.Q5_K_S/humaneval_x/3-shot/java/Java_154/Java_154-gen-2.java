        String rotated_word = b + b;
        for (int i = 0; i < a.length(); i++) {
            for (int j = 0; j < b.length(); j++) {
                if (rotated_word.contains(a.substring(i, i + b.length()))) {
                    return true;
                }
            }
        }
        return false;
    }
}

