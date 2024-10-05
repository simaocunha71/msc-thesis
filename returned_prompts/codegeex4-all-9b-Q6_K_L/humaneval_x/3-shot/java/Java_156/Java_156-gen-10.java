        String[] nums = {"", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix"};
        String[] tens = {"", "x", "xx", "xxx", "xl", "l", "lx", "lxx", "lxxx", "xc"};
        String[] hundreds = {"", "c", "cc", "ccc", "cd", "d", "dc", "dcc", "dcc", "cm"};
        String[] thousands = {"", "m", "mm", "mmm"};

        return thousands[number / 1000] + hundreds[number % 1000 / 100] + tens[number % 100 / 10] + nums[number % 10];
    }
}

