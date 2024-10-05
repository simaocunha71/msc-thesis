        int[] nums = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] romans = {"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};
        String result = "";

        for (int i = 0; i < nums.length; i++) {
            while (number >= nums[i]) {
                result += romans[i];
                number -= nums[i];
            }
        }
        return result;
    }
}

