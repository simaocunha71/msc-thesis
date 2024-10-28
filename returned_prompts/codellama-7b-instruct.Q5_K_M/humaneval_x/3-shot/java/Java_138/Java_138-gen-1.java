        if (n % 2 != 0) return false;
        int[] even_numbers = {2, 4, 6, 8};

        for (int i = 0; i < even_numbers.length; i++) {
            if (n - even_numbers[i] < 0) continue;
            else if (n - even_numbers[i] == 0) return true;
            else if (n - even_numbers[i] % 2 == 0) return false;
        }
        return false;
    }
}

