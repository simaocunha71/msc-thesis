        int whole_number = Integer.parseInt(value.substring(0, value.indexOf(".")));
        double fraction = Double.parseDouble(value.substring(value.indexOf(".")));
        int fraction_integer = (int) Math.round(fraction + Math.copysign(0.5, fraction));

        if (whole_number < 0 && fraction_integer < 0) {
            return -(whole_number + fraction_integer + 1);
        } else if (whole_number < 0) {
            return -(whole_number + fraction_integer);
        } else if (whole_number > 0) {
            return whole_number + fraction_integer;
        } else {
            return whole_number + fraction_integer + 1;
        }
    }
}

