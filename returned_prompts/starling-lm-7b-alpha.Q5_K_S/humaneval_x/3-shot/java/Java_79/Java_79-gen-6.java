        StringBuilder binary_string = new StringBuilder();
        binary_string.append("db");

        while (decimal > 0) {
            binary_string.append(decimal % 2);
            decimal /= 2;
        }

        binary_string.append("db");
        return binary_string.toString();
    }
}

