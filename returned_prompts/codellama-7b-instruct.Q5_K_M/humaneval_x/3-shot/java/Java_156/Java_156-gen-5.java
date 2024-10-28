        String[] num_names = {
            "m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"
        };

        String[] num_values = {
            "1000", "900", "500", "400", "100", "90", "50", "40", "10", "9", "5", "4", "1"
        };

        int index = 0;
        String result = "";

        while (number > 0) {
            int value = Integer.parseInt(num_values[index]);
            int count = number / value;
            number -= value * count;
            result += String.join("", Collections.nCopies(count, num_names[index]));
            index += 1;
        }
        return result;
    }
}

