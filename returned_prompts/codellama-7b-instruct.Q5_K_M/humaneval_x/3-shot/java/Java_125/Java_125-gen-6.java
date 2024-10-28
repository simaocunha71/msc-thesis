        if (txt.matches("\\s")) return txt.split("\\s+");
        if (txt.matches("\\,")) return txt.split("\\,+");
        int lower_case_count = 0;
        for (char c : txt.toCharArray()) {
            if (Character.isLowerCase(c)) lower_case_count += 1;
        }
        return lower_case_count;
    }
}

