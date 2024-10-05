        int number = N;
        int binary_sum = 0;
        String binary_number = "";
        while (number != 0) {
            binary_sum += number % 2;
            number /= 2;
        }
        while (binary_sum != 0) {
            binary_number += String.valueOf(binary_sum % 2);
            binary_sum /= 2;
        }
        return binary_number.reverse();
    }
}

