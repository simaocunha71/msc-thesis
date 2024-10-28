        int sum = array.get(0) + array.get(array.size() - 1);

        ArrayList<Integer> copy = new ArrayList<>(array);
        Collections.sort(copy);

        return (sum % 2 == 0) ? new ArrayList<>(Collections.reverseOrder(copy)) : copy;
    }
}

