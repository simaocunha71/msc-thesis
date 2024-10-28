        StringBuilder result = new StringBuilder();

        while (x != 0) {
            int remainder = x % base;
            result.append(remainder);
            x = x / base;
        }

        return result.reverse().toString();
    }
}

