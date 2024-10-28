        StringBuilder result = new StringBuilder();
        int quotient = x;

        while (quotient > 0) {
            int remainder = quotient % base;
            result.insert(0, remainder);
            quotient = quotient / base;
        }

        return result.toString();
    }
}

