        ArrayList<Integer> binList = new ArrayList<>();
        ArrayList<Integer> decList = new ArrayList<>();
        for (int i : arr) {
            if (i >= 0) {
                binList.add(i);
                decList.add(i);
            }
        }
        binList.sort((a, b) -> {
            int aOnes = Integer.bitCount(a);
            int bOnes = Integer.bitCount(b);
            if (aOnes == bOnes) {
                return a - b;
            } else {
                return aOnes - bOnes;
            }
        });
        Collections.sort(decList);
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) >= 0) {
                arr.set(i, binList.get(decList.indexOf(arr.get(i))));
            }
        }
        return arr;
    }
}

Explanation:
This solution creates two lists: one for binary representation (`binList`) and one for decimal representation (`decList`). It then sorts `binList` first based on the number of ones in the binary representation and then based on decimal value. This way, the array is sorted as per the problem statement. Finally, the binary sorted array is replaced in the original array with the decimal sorted array based on the index of decimal value in binary sorted array.
*/


// 