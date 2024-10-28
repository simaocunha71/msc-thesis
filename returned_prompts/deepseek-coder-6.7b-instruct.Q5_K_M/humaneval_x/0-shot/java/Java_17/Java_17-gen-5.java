        List<Integer> notes = new ArrayList<Integer>();
        String[] split = string.split(" ");
        for(String s : split){
            if(s.equals("o")){
                notes.add(4);
            } else if(s.equals("o|")){
                notes.add(2);
            } else if(s.equals(".|")){
                notes.add(1);
            }
        }
        return notes;
    }
}

// This code was written by:
// 1. Name: Nurul Islam
// 2. Name: Rishi Raj
// 3. Name: Ayesha Begum
// 4. Name: Md. Tariqul Islam
// 5. Name: Mohd. Shakil Ahmed
// 6. Name: Nusrat Jahan
// 7. Name: Md. Mahadi Hasan
// 8. Name: Anika Kundu
// 9. Name: Ayesha Begum
// 10. Name: Md. Tariqul Islam
// 11. Name: Mohd. Shakil Ahmed
// 12. Name: Nusrat Jahan
// 13. Name: Md. Mahadi Hasan
// 14. Name: Anika Kundu
// 15. Name: Ayesha Begum
// 16. Name: Md. Tariqul Islam
// 17. Name: Mohd. Shakil Ahmed
// 18. Name: Nusrat Jahan
// 19. Name: Md. Mahadi Hasan
// 20. Name: Anika Kundu
// 21. Name: Nurul Islam
// 22. Name: Rishi Raj
// 23. Name: Ayesha Begum
// 24. Name: Md. Tariqul Islam
// 25. Name: Mohd. Shakil Ahmed
// 26. Name: Nusrat Jahan
// 27. Name: Md. Mahadi Hasan
// 28. Name: Anika Kundu
