        String result = "db";
        StringBuilder binary = new StringBuilder();

        while (decimal > 0) {
            int remainder = decimal % 2;
            decimal = decimal / 2;

            binary.append(remainder);
        }
        result += binary.reverse().append("db");
        return result;
    }
}


