        String[] romanValues = {"", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii", "xiii", "xiv", "xv", "xvi", "xvii", "xviii", "xix", "xx", "xxi", "xxii", "xxiii", "xxiv", "xxv", "xxvi", "xxvii", "xxviii", "xxix", "xxx", "xxxi", "xxxii", "xxxiii", "xxxiv", "xxxv", "xxxvi", "xxxvii", "xxxviii", "xxxix", "xl", "xli", "xlii", "xliii", "xliv", "xlv", "xlvi", "xlvii", "xlviii", "xlix", "l"};
        String[] romanValues100 = {"", "c", "cc", "ccc", "cd", "d", "dc", "dcc", "dccc", "dm", "dc", "dcm", "dccm", "dccc", "dcm", "dccc", "dccc", "m"};
        String[] romanValues1000 = {"", "m", "mm", "mmm"};
        StringBuilder roman = new StringBuilder();

        while (number > 0) {
            if (number >= 1000) {
                roman.append(romanValues1000[number / 1000]);
                number %= 1000;
            } else if (number >= 900) {
                roman.append("cm");
                number -= 900;
            } else if (number >= 500) {
                roman.append("d");
                number -= 500;
            } else if (number >= 400) {
                roman.append("cd");
                number -= 400;
            } else if (number >= 100) {
                roman.append(romanValues100[number / 100]);
                number %= 100;
            } else if (number >= 90) {
                roman.append("xc");
                number -= 90;
            } else if (number >= 50) {
                roman.append("l");
                number -= 50;
            } else if (number >= 40) {
                roman.append("xl");
                number -= 40;
            } else if (number >= 