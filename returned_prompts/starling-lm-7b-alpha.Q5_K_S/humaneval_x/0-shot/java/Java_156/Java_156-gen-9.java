        int[] nums = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] romans = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        List<String> result = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            while (number >= nums[i]) {
                result.add(romans[i]);
                number -= nums[i];
            }
        }

        return String.join("", result);
    }
}


# Python

def intToMiniRoman(number):
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    result = []

    for i, n in enumerate(nums):
        while number >= n:
            result.append(romans[i])
            number -= n

    return "".join(result)

# Python

def intToMiniRoman(number):
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    result = []

    for i, n in enumerate(nums):
