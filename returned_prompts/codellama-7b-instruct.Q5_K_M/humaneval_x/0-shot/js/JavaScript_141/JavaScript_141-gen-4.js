const fileNameCheck = (file_name) => {
    if (file_name.match(/[0-9].*[0-9].*[0-9]/)) {
        return 'No'
    }
    if (file_name.indexOf('.') === -1) {
        return 'No'
    }
    if (file_name[0] > 'Z' || file_name[0] < 'A') {
        return 'No'
    }
    if (file_name.substr(file_name.lastIndexOf('.') + 1) !== 'txt' && file_name.substr(file_name.lastIndexOf('.') + 1) !== 'exe' && file_name.substr(file_name.lastIndexOf('.') + 1) !== 'dll') {
        return 'No'
    }
    return 'Yes'
}
