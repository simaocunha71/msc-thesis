        int count = 0;
        for (int i : nums) {
            String s = i + "";
            if (s.charAt(0) % 2 != 0 && s.charAt(s.length() - 1) % 2 != 0 && i > 10) {
                count += 1;
            }
        }
        return count;
    }
}

