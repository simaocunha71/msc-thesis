    String[] nums = numbers.split(" ");
    Arrays.sort(nums);
    StringBuilder sb = new StringBuilder();
    for (String num : nums) {
        sb.append(num).append(" ");
    }
    return sb.toString().trim();
}
}

