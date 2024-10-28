        int result = 0;
        for (int number : nums) {
            String number_str = number + "";
            if (number_str.length() != 2) continue;
            if (number_str.charAt(0) % 2 == 1 && number_str.charAt(1) % 2 == 1)
                result += 1;
        }
        return result;
    }
}

