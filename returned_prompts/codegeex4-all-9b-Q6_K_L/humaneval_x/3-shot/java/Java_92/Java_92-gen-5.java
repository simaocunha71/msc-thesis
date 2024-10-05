        if (x instanceof Integer && y instanceof Integer && z instanceof Integer) {
            int num1 = (int) x;
            int num2 = (int) y;
            int num3 = (int) z;

            return (num1 == num2 + num3) || (num2 == num1 + num3) || (num3 == num1 + num2);
        }

        return false;
    }
}

