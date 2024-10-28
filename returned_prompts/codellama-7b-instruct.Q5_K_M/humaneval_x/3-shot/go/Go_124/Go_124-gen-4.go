    var date_splited = strings.Split(date, "-")
    if len(date_splited)!=3{
        return false
    }
    var month, day, year = date_splited[0], date_splited[1], date_splited[2]
    if len(month)>2 || len(day)>2 || len(year)>4{
        return false
    }

    var month_num, _ = strconv.Atoi(month)
    var day_num, _ = strconv.Atoi(day)
    var year_num, _ = strconv.Atoi(year)
    if month_num<1 || month_num>12 || day_num<1 || day_num>31 {
        return false
    }

    if month_num==2 && day_num<1 || day_num>28{
        return false
    }
    if (month_num==1 || month_num==3 || month_num==5 || month_num==7 || month_num==8 || month_num==10 || month_num==12) && day_num<1 || day_num>31 {
        return false
    }
    if (month_num==4 || month_num==6 || month_num==9 || month_num==11) && day_num<1 || day_num>30 {
        return false
    }
    return true
}



