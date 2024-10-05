    var result strings.Builder
    var thousands, hundreds, tens, units byte = 1000, 100, 10, 1
    var thousands_symbol, hundreds_symbol, tens_symbol, units_symbol byte = 'm', 'c', 'x', 'i'

    for number > 0 {
        if number >= thousands {
            result.WriteByte(thousands_symbol)
            number -= thousands
        }
        if number >= hundreds {
            result.WriteByte(hundreds_symbol)
            number -= hundreds
        }
        if number >= tens {
            result.WriteByte(tens_symbol)
            number -= tens
        }
        if number >= units {
            result.WriteByte(units_symbol)
            number -= units
        }
    }
    return result.String()
}



