        String number_str = "" + x;
        int number_length = number_str.length();
        int shift_by = (number_length + shift) % number_length;
        return number_str.substring(shift_by) + number_str.substring(0, shift_by);
    }
}

