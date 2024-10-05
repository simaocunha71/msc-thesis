        String[] ones = {"i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix"};
        String[] tens = {"x", "xx", "xxx", "xl", "l", "lx", "lxx", "lxxx", "xc"};
        String[] hundreds = {"c", "cc", "ccc", "cd", "d", "dc", "dcc", "dcc", "cm"};
        String[] thousands = {"m", "mm", "mmm"};

        int num = number;
        String roman = "";

        if (num >= 1000) {
            roman += thousands[num / 1000 - 1];
            num %= 1000;
        }

        if (num >= 100) {
            roman += hundreds[num / 100 - 1];
            num %= 100;
        }

        if (num >= 10) {
            roman += tens[num / 10 - 1];
            num %= 10;
        }

        if (num >= 1) {
            roman += ones[num - 1];
        }

        return roman;
    }
}

