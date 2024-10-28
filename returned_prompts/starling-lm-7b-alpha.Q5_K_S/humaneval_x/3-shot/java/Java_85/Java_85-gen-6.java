        int result = 0;
        for (int i = 0; i < lst.size(); i++) {
            int n = lst.get(i);
            if (n % 2 == 0 && i % 2 == 0) {
                result += n;
            }
        }
        return result;
    }
}

