        int[] nums = new int[arr.size()];
        for (int i = 0; i < arr.size(); i++) {
            nums[i] = arr.get(i);
        }

        int left = 0;
        int right = arr.size() - 1;

        while (left < right) {
            if (nums[left] != nums[right]) {
                nums[left] = nums[right] = Math.abs(nums[left] - nums[right]);
            }
            left++;
            right--;
        }

        int min = nums[0];
        for (int i = 1; i < nums.length; i++) {
            min = Math.min(nums[i], min);
        }
        return min;
    }
}

