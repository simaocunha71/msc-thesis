        String number = String.valueOf(x);
        int length = number.length();
        int shift_by = shift % length;

        return number.substring(length - shift_by) + number.substring(0, length - shift_by);
    }
}

