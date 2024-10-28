import  (
    "strings"
)

func FileNameCheck(file_name string) string {
    if count := strings.Count(file_name, "."); count != 1 {
        return "No"
    }

    splitted := strings.Split(file_name, ".")
    if !(splitted[0][0] >= 'a' && splitted[0][0] <= 'z' || splitted[0][0] >= 'A' && splitted[0][0] <= 'Z') || splitted[0] == "" {
        return "No"
    }

    if len(strings.Join(strings.Fields(splitted[0]), "")) > 3 {
        return "No"
    }

    if splitted[1] != "txt" && splitted[1] != "exe" && splitted[1] != "d