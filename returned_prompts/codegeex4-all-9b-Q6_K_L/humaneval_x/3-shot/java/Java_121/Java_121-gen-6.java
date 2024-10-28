        int result = 0;
        for (int i = 0; i < lst.size(); i += 2) {
            int num = lst.get(i);
            if (num % 2 == 1) {
                result += num;
            }
        }
        return result;
    }
}

