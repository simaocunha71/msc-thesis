        int integer_part = Integer.parseInt(value.substring(0, value.indexOf(".")));
        int leftover_part = Integer.parseInt(value.substring(value.indexOf(".")+1));
        int result = integer_part + (leftover_part > 0 ? 1 : -1);
        return result;
    }
}

