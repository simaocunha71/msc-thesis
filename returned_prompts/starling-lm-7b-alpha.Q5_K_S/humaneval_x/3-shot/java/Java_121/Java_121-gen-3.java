        int result = 0;
        int index = 0;
        for (int elem : lst) {
            if (index % 2 == 0 && elem % 2 != 0) {
                result += elem;
            }
            index += 1;
        }
        return result;
    }
}

