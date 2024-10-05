        int count = 0;
        String lower = s.toLowerCase();
        for(int i = 0; i < s.length(); i++){
            char c = lower.charAt(i);
            if(c == 'a'|| c == 'e'|| c == 'i'|| c == 'o'|| c == 'u'){
                count++;
            }
        }
        if(s.charAt(s.length()-1) == 'y'){
            count++;
        }
        return count;
    }
}

*/

//