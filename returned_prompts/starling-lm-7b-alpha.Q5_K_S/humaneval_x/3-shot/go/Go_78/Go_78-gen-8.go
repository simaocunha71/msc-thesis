    prime_digits := map[rune]bool{'0':false,'1':false,'2':true,'3':true,'4':false,'5':true,'6':false,'7':true,'8':false,'9':false,'A':true,'B':true,'C':false,'D':true,'E':false,'F':false}
    count := 0
    for _,c := range num{
        if prime_digits[c]{
            count++
        }
    }
    return count
}



