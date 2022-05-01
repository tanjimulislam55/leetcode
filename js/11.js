const isPalindrome = (num) => {
    const x = num.toString()
    let first = 0
    let last = x.length - 1
    while (first < last) {
        if (x[first] === x[last]) {
            first++
            last--
        } else {
            return false
        }
    }
    return true
};

console.log(isPalindrome(121))