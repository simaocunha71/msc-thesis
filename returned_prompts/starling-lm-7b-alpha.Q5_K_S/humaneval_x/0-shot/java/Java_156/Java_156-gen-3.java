        int[] nums = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] strs = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < nums.length; i++) {
            while (number >= nums[i]) {
                sb.append(strs[i]);
                number -= nums[i];
            }
        }

        return sb.toString();
    }
}

# Python Solution
# >>> intToMiniRoman(19)
# 'xix'
# >>> intToMiniRoman(152)
# 'clii'
# >>> intToMiniRoman(426)
# 'cdxxvi'
def intToMiniRoman(number):
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    strs = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    sb = ""
    for i in range(len(nums)):
        while number >= nums[i]:
            sb += strs[i]
            number -= nums[i]
    return sb


# Python Solution - Optimized
def intToMiniRoman(number):
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    strs = ["M", "CM", "