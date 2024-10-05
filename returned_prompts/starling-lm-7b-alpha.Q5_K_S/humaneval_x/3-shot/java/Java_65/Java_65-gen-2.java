        StringBuilder result = new StringBuilder();
        String digits = String.valueOf(x);
        int length = digits.length();
        int target_index = (length + shift - 1) % length;
        result.append(digits.charAt(target_index));
        for (int i = 0; i < length; i++) {
            if (i != target_index) {
                result.append(digits.charAt((i + 1) % length));
            }
        }
        return result.toString();
    }
}

