        int sum = 0;
        for (char c : s.toCharArray()) {
            if (c >= 'A' && c <= 'Z') {
                sum += c;
            }
        }
        return sum;
    }
}

