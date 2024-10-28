        int[] sides = {a, b, c};
        Arrays.sort(sides);
        return sides[2] * sides[2] == sides[0] * sides[0] + sides[1] * sides[1];
    }
}

