    layout := "2006-01-02 15:04:05.000"
    t, err := time.Parse(layout, timestamp)
    if err != nil {
        panic(err)
    }
    return t.UnixNano() /