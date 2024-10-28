        String result = "";
        if (decimal == 0) return "db0db";
        while (decimal > 0) {
            result = (decimal % 2 == 0) ? "0" : "1" + result;
            decimal /= 2;
        }
        return "db" + result + "db";
    }
}

