    var total_seconds int
    hours_minutes_seconds := strings.Split(time_string, ":")
    hours, _ := strconv.Atoi(hours_minutes_seconds[0])
    minutes, _ := strconv.Atoi(hours_minutes_seconds[1])
    seconds, _ := strconv.Atoi(hours_minutes_seconds[2])
    total_seconds += (hours * 3600) + (minutes * 60) + seconds
    return total_seconds
}



