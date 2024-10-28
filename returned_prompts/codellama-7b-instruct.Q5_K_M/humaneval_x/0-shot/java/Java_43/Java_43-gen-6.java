for(int i =0; i<l.size(); i++){
    for(int j=i+1; j<l.size(); j++){
        if(l.get(i)+l.get(j)==0){
            return true;
        }
    }
}

return false;

    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.pairsSumToZero(Arrays.asList(1, 3, 5, 0)));

        System.out.println(s.pairsSumToZero(Arrays.asList(1, 3, -2, 1)));

        System.out.println(s.pairsSumToZero(Arrays.asList(1, 2, 3, 7)));

        System.out.println(s.pairsSumToZero(Arrays.asList(2, 4, -5, 3, 5, 7)));

        System.out.println(s.pairsSumToZero(Arrays.asList(1)));
    }
}
