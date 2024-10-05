        int result = 0;
        int index = 0;
        for (int i : lst) {
            if (i % 2 == 0 && index % 2 == 1) {
                result += i;
            }
            index += 1;
        }
        return result;
    }
}

