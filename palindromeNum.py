def isPalindrome(x):
        rev_int = x
        new_int = 0

        while rev_int != 0:
            last_digit  = rev_int % 10
            rev_int = rev_int // 10
            new_int = 10 * new_int + last_digit

        return new_int == x

answer = isPalindrome(1271)

print(answer)