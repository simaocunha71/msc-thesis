        int result = 0;
        for (int i = 0; i < lst.size(); i++) {
            int element = lst.get(i);
            if (element % 2 == 0 && i % 2 == 0) {
                result += element;
            }
        }
        return result;
    }
}

