        for (int d : String.valueOf(number).chars().map(c -> c - '0').toArray()) {
            if (d % 2 == 0) return true;
        }
        return false;
    }
}

