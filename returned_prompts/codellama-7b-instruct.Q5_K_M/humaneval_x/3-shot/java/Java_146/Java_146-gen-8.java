        int result = 0;
        for (int num : nums) {
            if (num > 10 && ((num % 10 > 1 && num % 10 < 9) || (num % 10 == 1 && num % 100 > 10 && num % 100 < 20)))
                result += 1;
        }
        return result;
    }
}

