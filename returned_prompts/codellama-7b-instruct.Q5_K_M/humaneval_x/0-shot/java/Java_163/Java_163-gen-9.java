        List<Integer> result = new ArrayList<>();

        for (int i = a; i <= b; i++) {
            int lastDigit = i % 10;
            if (lastDigit % 2 == 0) {
                result.add(i);
            }
        }

        return result;
    }
}


