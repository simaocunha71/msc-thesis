        return arr.stream().sorted((a, b) -> {
            int onesA = Integer.bitCount(a);
            int onesB = Integer.bitCount(b);
            if (onesA != onesB) return onesA - onesB;
            return a - b;
        }).collect(Collectors.toList());

    }
}

