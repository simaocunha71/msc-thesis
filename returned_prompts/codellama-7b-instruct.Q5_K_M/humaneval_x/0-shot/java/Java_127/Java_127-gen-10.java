        int[] intArray1 = new int[2];
        int[] intArray2 = new int[2];
        intArray1[0] = interval1.get(0);
        intArray1[1] = interval1.get(1);
        intArray2[0] = interval2.get(0);
        intArray2[1] = interval2.get(1);

        int[] intArray3 = new int[2];
        intArray3[0] = Math.max(intArray1[0], intArray2[0]);
        intArray3[1] = Math.min(intArray1[1], intArray2[1]);

        int intersectionLength = intArray3[1] - intArray3[0] + 1;

        if(intArray3[0] < intArray3[1] && intersectionLength > 0) {
            return "YES";
        }
        return "NO";

    }
}



