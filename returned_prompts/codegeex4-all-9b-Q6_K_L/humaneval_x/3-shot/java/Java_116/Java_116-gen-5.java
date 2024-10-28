        arr.sort((o1, o2) -> {
            String binary1 = Integer.toBinaryString(o1);
            String binary2 = Integer.toBinaryString(o2);
            int count1 = 0;
            int count2 = 0;
            for (int i = 0; i < binary1.length(); i++) {
                if (binary1.charAt(i) == '1') count1++;
            }
            for (int i = 0; i < binary2.length(); i++) {
                if (binary2.charAt(i) == '1') count2++;
            }
            if (count1 == count2) return o1 - o2;
            else return count1 - count2;
        });
        return arr;
    }
}

