        if(arr.isEmpty())
            return true;

        int[] arr1 = new int[arr.size()];
        for(int i=0;i<arr.size();i++)
            arr1[i] = arr.get(i);

        Arrays.sort(arr1);

        int max = arr1[arr1.length-1];

        if(max < arr.get(0))
            return true;

        return false;
    }
}
