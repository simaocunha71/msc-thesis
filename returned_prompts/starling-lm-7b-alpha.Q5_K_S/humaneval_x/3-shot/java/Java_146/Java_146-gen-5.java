        int result = 0;
        for (int i : nums) {
            if (i > 10 && (i / 10 % 10) % 2 == 1 && i % 10 % 2 == 1) result += 1;
        }
        return result;
    }
}

