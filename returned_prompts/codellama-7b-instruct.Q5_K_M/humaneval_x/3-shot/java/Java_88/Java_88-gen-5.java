        int sum = 0;
        for (Integer i : array) {
            sum += i;
        }

        if (sum % 2 == 0) {
            return array;
        } else {
            Collections.sort(array, Collections.reverseOrder());
            return array;
        }
    }
}

