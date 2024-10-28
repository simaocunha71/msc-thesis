        String result = "db";

        while (decimal > 0) {
            result = (decimal % 2) + result;
            decimal /= 2;
        }

        return result + "db";
    }
}

