        int count = 0;

        for (int i = 0; i < num.length(); i++) {
            int hex = Character.getNumericValue(num.charAt(i));

            if (hex == 10 || hex == 11 || hex == 12 || hex == 13 || hex == 14 || hex == 15) {
                count++;
            }
        }

        return count;
    }
}

