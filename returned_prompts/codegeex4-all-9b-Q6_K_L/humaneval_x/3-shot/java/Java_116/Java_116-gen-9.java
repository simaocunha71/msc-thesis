        arr.sort((a, b) -> {
            int onesA = Integer.bitCount(a);
            int onesB = Integer.bitCount(b);
            if (onesA != onesB) return onesA - onesB;
            else return a - b;
        });
        return arr;
    }
}

