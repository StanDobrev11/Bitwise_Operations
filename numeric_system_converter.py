"""This is a binary - decimal - hexadecimal and vice-versa converter."""


# TODO Consider negative values of the numbers signed/unsigned binary numbers.


def check_valid(bin_num: str) -> bool:
    """
    This function validates binary input and adds leading zeros.
    :param bin_num: string
    :return boolean
    """
    for symbol in bin_num:
        if int(symbol) > 1:
            return False
    return True


def binary_to_decimal(bin_num: str) -> int:
    """
    This function converts a binary number to decimal number;
    :param bin_num: string, containing binary information (0 & 1) only;
    """
    if check_valid(bin_num):
        base = 2
        power = len(bin_num) - 1
        result = 0
        for symbol in bin_num:
            result += int(symbol) * (base ** power)
            power -= 1
        return result
    raise ValueError


def decimal_to_binary(decimal_num: int) -> str:
    """
    This function converts a binary number to decimal number;
    :param decimal_num: integer
    """
    base = 2
    result = ''
    while decimal_num >= 1:
        remainder = decimal_num % 2
        decimal_num //= base
        result = str(remainder) + result
    return result


def hexadecimal_to_decimal(hex_num: str) -> int:
    """
    This function converts hexadecimal numbers to decimal numbers:
    :param hex_num: string
    """
    hex_letters_as_numbers = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    if '0x' in hex_num:
        hex_num = hex_num.replace('0x', '')
    hex_num = hex_num[::-1]
    base = 16
    result = 0
    power = 0
    for idx in range(len(hex_num)):
        if hex_num[idx].isalpha():
            result += (hex_letters_as_numbers[hex_num[idx].upper()]) * (base ** power)
        else:
            result += int(hex_num[idx]) * (base ** power)
        power += 1
    return result


def decimal_to_hexadecimal(decimal_num: int) -> str:
    """
    This function convert decimal number to hexadecimal.
    :param decimal_num: integer
    """

    numbers_as_hex_letters = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    base = 16
    result = ''
    while decimal_num >= 1:
        remainder = decimal_num % base
        if remainder in numbers_as_hex_letters:
            remainder = numbers_as_hex_letters[remainder]
        result = str(remainder) + result
        decimal_num //= base
    result = '0x' + result
    return result


def hexadecimal_to_binary(hex_num: str) -> str:
    """
    This function converts hexadecimal to binary numbers using other functions.
    :param hex_num: string
    """
    result = hexadecimal_to_decimal(hex_num)
    return decimal_to_binary(result)


def binary_to_hexadecimal(bin_num: str) -> str:
    """
    This function converts binary to hexadecimal numbers using other functions.
    :param bin_num: string
    """
    result = binary_to_decimal(bin_num)
    return decimal_to_hexadecimal(result)


# num = input("Enter number in decimal, binary or hexadecimal: ")
# operation = input("Select operation: \n"
#                   "Binary to Decimal (1) or \n"
#                   "Decimal to Binary (2) or \n"
#                   "Hexadecimal to Decimal(3) or \n"
#                   "Decimal to Hexadecimal(4) or \n"
#                   "Hexadecimal to Binary(5) or \n"
#                   "Binary to Hexadecimal(6): ").lower()
#
# if operation == '1':
#     print(binary_to_decimal(num))
# elif operation == '2':
#     num = int(num)
#     print(decimal_to_binary(num))
# elif operation == '3':
#     print(hexadecimal_to_decimal(num))
# elif operation == '4':
#     num = int(num)
#     print(decimal_to_hexadecimal(num))
# elif operation == '5':
#     print(hexadecimal_to_binary(num))
# elif operation == '6':
#     print(binary_to_hexadecimal(num))
# else:
#     print("Wrong input")
