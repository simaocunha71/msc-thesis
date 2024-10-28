    var result int

    for _, row := range grid{
        for _, value := range row{
            if value==1{
                result += 1
            }
        }
    }

    if result<=capacity{
        return 0
    }

    var row_count, column_count int

    for _, row := range grid{
        if len(row) > column_count{
            column_count = len(row)
        }
    }

    for i:=0; i<column_count; i++{
        for _, row := range grid{
            if row[i]==1{
                row_count += 1
            }
        }
        if row_count>capacity{
            return i
        }
    }

    return 0
}



