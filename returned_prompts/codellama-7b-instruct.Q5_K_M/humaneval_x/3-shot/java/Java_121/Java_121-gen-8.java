        int result = 0;
        for (int i = 0; i < lst.size(); i += 2) {
            if (lst.get(i) % 2 == 1) {
                result += lst.get(i);
            }
        }
        return result;
    }
}

