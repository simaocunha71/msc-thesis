        int count = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums.get(i) > 10 && (nums.get(i) % 10 > 1 || nums.get(i) % 10 < 9)) {
                count += 1;
            }
        }
        return count;
    }
}

