        int sum = 0;
        for (char c : s.toCharArray()) {
            int c_ascii = (int) c;
            if (c_ascii >= 65 && c_ascii <= 90) {
                sum += c_ascii;
            }
        }
        return sum;
    }
}

