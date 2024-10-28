        String number_str = String.valueOf(number);
        String reverse = "";
        for (int i = number_str.length() - 1; i >= 0; i--) {
            reverse += number_str.charAt(i);
        }
        return number_str.equals(reverse);
    }
}

