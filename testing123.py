import pandas as pd
from typing import Union, MutableSequence
from pprint import pprint

# columns = ['trade_code', 'trade_value']
# data = {'trade_code': [1, 3, 5, 6, 7], 'trade_value': [2, 3, 4, 5, 6]}
# data2 = {'trade_code': [2, 3, 4, 6, 8], 'trade_value': [1, 3, 3, 5, 6]}
# df1 = pd.DataFrame(data)
# df2 = pd.DataFrame(data2)
# df3 = df1.merge(df2, on='trade_code')
# # df1['trade_code'] = [1, 2, 3, 4, 5]
# # df1['trade_value'] = [10, 20, 30, 40, 50]

# # print(df1.head())

# # df2['trade_code'] = [1, 2, 3, 4, 5]
# # df2['trade_value'] = [10, 20, 30, 40, 50]
# print('Dataframe 3 below:\n')
# print(df3)

def determine_armstrong_number(num: Union[MutableSequence[int], MutableSequence[float]]) -> bool:
    all_digits: MutableSequence[int] = list()
    original_num = num
    if isinstance(num, float):
        num = int(num)
        while num > 0:
            digit = num % 10
            all_digits.append(pow(digit, 3))
            num //= 10
        return f'{int(original_num)} -> is Armstrong' if sum(all_digits) == original_num else f'{int(original_num)} -> is NOT Armstrong'
    elif isinstance(num, list):
        # print('int list detected...')
        all_digits.clear()
        integer_conv_nos = [int(each_num) for each_num in num if isinstance(each_num, int)]
        test_results: MutableSequence[str] = list()
        message: str = str()
        for test_num in integer_conv_nos:
            all_digits.clear()
            original_num = test_num
            while test_num > 0:
                digit = test_num % 10
                all_digits.append(pow(digit, 3))
                test_num //= 10
            message = f'{int(original_num)} -> is Armstrong'.upper() if sum(all_digits) == original_num else f' {int(original_num)} -> is NOT Armstrong'.lower()
            test_results.append(message)
        print(' '.join(test_results))
    else:   # Default will be the integer valued list
        print('farthest else condition flag.')
        if isinstance(num, list):
            default_integer_list = [x for x in num if isinstance(num, int)]
            all_digits: MutableSequence[int] = list()
            test_results: MutableSequence[str] = list()
            for each_num in default_integer_list:
                original_num = each_num
                while each_num > 0:
                    digit = each_num % 10
                    all_digits.append(pow(digit, 3))
                    each_num //= 10
                message = f'{int(original_num)} -> is Armstrong'.upper() if sum(all_digits) == original_num else f' {int(original_num)} -> is NOT Armstrong'.lower()
                test_results.append(message)
            print(' '.join(test_results))
        else:
            while num > 0:
                digit = num % 10
                all_digits.append(pow(digit, 3))
                num //= 10
            return f'{int(original_num)} -> is Armstrong'.upper() if sum(all_digits) == original_num else f' {int(original_num)} -> is NOT Armstrong'.lower()

# Test case - 1
def check_for_test_case_1():
    floating_point_list = [float(x) for x in range(150, 161)]
    integer_point_list = [float(x) for x in range(150, 161)]
    print(list(map(lambda x: determine_armstrong_number(x), floating_point_list)))
    print(determine_armstrong_number(integer_point_list))

# Test case - 2
def check_for_test_case_2():
    struct_choice = int(input('Choose a proper data stucture:\n1> List\n2> Individual integer:\n'))
    # print('choices'.swapcase())
    if not isinstance(struct_choice, int):
        raise ValueError('Choose a valid option from the list.')
    elif isinstance(struct_choice, int) and (struct_choice <= 0 or struct_choice > 2):
        raise ValueError('Dear, you can select only from the given list of options,\n I hope you have worn your glasses.')
    else:
        if int(struct_choice) == 1:
            num_range = input('enter a valid number range to store as per your choice:\t'.capitalize())
            all_chosen_nos: MutableSequence[Union[int, float]] = list()
            for i in range(1, int(num_range) + 1):
                num_inputs = input(f'Enter your preferred input number {i}:\t')
                all_chosen_nos.append(num_inputs)
            determine_armstrong_number([int(x) for x in all_chosen_nos])
            print('Results successful.')
        elif int(struct_choice) == 2:
            test_num = int(input('Enter the number you want to check:\t'))
            if test_num <= 0:
                raise ValueError('stop kidding, enter a valid number to check. Try again.')
            # else:
            print(determine_armstrong_number(test_num))
        else:
            raise ValueError('There seems to be an issue, try again later. Apologies for the inconvenience caused.')

# Evaluate both the test cases
check_for_test_case_1()
check_for_test_case_2()