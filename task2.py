# Написать функцию, которая определяет,
# является ли целое число палиндромом.
# Числовой палиндром читается слева направо
# и справа налево одинаково, например 101. 

# Пример работы функции:
# is_palindrome(353) # True
# is_palindrome(-111) # False
# is_palindrome(42) # False

def is_palindrome(num):
    palindrome_input_list = [int(x) for x in str(num)]
    palindrome_reverse = palindrome_input_list[ -1:: -1]
    if palindrome_input_list == palindrome_reverse:
        print('this is pslindrome')
    else:
        print('this is not palindrome')


is_palindrome(363)
