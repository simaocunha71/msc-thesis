        int count = 0;
        for (char c : value.toCharArray()) {
            if (Character.isUpperCase(c)) {
                count += 1;
            }
        }
        return count;
    }
}

