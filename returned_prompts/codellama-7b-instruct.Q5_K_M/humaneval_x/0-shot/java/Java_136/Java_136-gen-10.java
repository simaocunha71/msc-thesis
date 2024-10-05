        int smallest = -1;
        int largest = -1;

        for(int i : lst){
            if(i < 0 && smallest == -1){
                smallest = i;
            }
            if(i > 0 && largest == -1){
                largest = i;
            }
            if(i < 0 && largest != -1){
                largest = i;
            }
            if(i > 0 && smallest != -1){
                smallest = i;
            }
        }
        if(smallest != -1 && largest != -1){
            return Arrays.asList(Optional.of(largest), Optional.of(smallest));
        }
        if(smallest == -1 && largest == -1){
            return Arrays.asList(Optional.empty(), Optional.empty());
        }
        if(smallest != -1 && largest == -1){
            return Arrays.asList(Optional.empty(), Optional.of(smallest));
        }
        if(smallest == -1 && largest != -1){
            return Arrays.asList(Optional.of(largest), Optional.empty());
        }
        return Arrays.asList(Optional.empty(), Optional.empty());

    }
}

