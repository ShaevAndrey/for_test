function p (word) {
    let left_cursor = 0
    let right_cursor = word.length - 1
    console.log(left_cursor, right_cursor)
    while (left_cursor < right_cursor) {
        console.log(word[left_cursor], word[right_cursor])
        if (word[left_cursor]!=word[right_cursor]) {
            return false}
        left_cursor = left_cursor + 1
        right_cursor = left_cursor - 1             
    }
    return true
    
}

console.log(p('wow'))
