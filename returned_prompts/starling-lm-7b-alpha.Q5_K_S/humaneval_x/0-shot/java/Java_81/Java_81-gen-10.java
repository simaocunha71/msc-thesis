    List<String> ans = new ArrayList<>();
    Collections.sort(grades);

    for(double g : grades){
        if(g > 4.0){
            ans.add("A+");
        }
        else if(g > 3.7){
            ans.add("A");
        }
        else if(g > 3.3){
            ans.add("A-");
        }
        else if(g > 3.0){
            ans.add("B+");
        }
        else if(g > 2.7){
            ans.add("B");
        }
        else if(g > 2.3){
            ans.add("B-");
        }
        else if(g > 2.0){
            ans.add("C+");
        }
        else if(g > 1.7){
            ans.add("C");
        }
        else if(g > 1.3){
            ans.add("C-");
        }
        else if(g > 1.0){
            ans.add("D+");
        }
        else if(g > 0.7){
            ans.add("D");
        }
        else if(g > 0.0){
            ans.add("D-");
        }
        else if(g >= 0.0){
            ans.add("E");
        }
    }

    return ans;
}
}




































































































































































