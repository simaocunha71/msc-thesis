        String[] romanNumbers = {"", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii", "xiii", "xiv", "xv", "xvi", "xvii", "xviii", "xix", "xx"};
        String[] romanNumbers100 = {"", "c", "cc", "ccc", "cd", "d", "dc", "dcc", "dccc", "cm", "cci", "ccii", "cciii", "cciv", "ccv", "ccvi", "ccvii", "ccviii", "ccix", "ccx"};
        String[] romanNumbers1000 = {"", "m", "mm", "mmm", "miv", "mv", "mvi", "mvii", "mviii", "mix", "mlx", "mxc", "mxci", "mxii", "mxiii", "mxiv", "mxv", "mxvi", "mxvii", "mxviii", "mxix", "mmx"};
        StringBuilder result = new StringBuilder();

        if (number >= 1000) {
            int thousands = number / 1000;
            for (int i = 0; i < thousands; i++) {
                result.append("m");
            }
            number = number % 1000;
        }

        if (number >= 100) {
            int hundreds = number / 100;
            result.append(romanNumbers100[hundreds]);
            number = number % 100;
        }

        if (number >= 10) {
            int tens = number / 10;
            result.append(romanNumbers[tens]);
            number = number % 10;
        }

        if (number > 0) {
            result.append(romanNumbers[number]);
        }

        return result.toString().toLowerCase();
    }
}

