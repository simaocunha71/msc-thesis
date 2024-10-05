        if (x <= 0) {
            return "";
        }
        String result = "";
        int length = (int) Math.log10(x) + 1;
        if (length == shift) {
            return "";
        }
        String[] nums = String.valueOf(x).split("");
        int numsLength = nums.length;
        int[] numsArray = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            numsArray[i] = Integer.parseInt(nums[i]);
        }
        if (shift > nums.length) {
            for (int i = nums.length - 1; i >= 0; i--) {
                result += numsArray[i];
            }
        } else {
            int[] shiftedNums = new int[nums.length];
            for (int i = 0; i < nums.length; i++) {
                if (i + shift < nums.length) {
                    shiftedNums[i] = numsArray[i + shift];
                } else {
                    shiftedNums[i] = numsArray[i + shift - nums.length];
                }
            }
            for (int i = 0; i < shiftedNums.length; i++) {
                result += shiftedNums[i];
            }
        }
        return result;
    }
}

