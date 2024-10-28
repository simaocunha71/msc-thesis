        int[] sides = new int[3];
        sides[0] = a;
        sides[1] = b;
        sides[2] = c;
        Arrays.sort(sides);
        return (sides[0] * sides[0] + sides[1] * sides[1]) == sides[2] * sides[2];
    }
}

