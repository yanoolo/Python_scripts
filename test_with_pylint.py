'''
A simple py script with 10/10 pylint 2.3.1 score
To test this with pylint. Run:
pylint -f colorized test_with_pylint.py -r yes
'''

def sum_integers():
    '''
    Assign two variables (integers)
    Print assigned variables
    Print the sum of assigned variables
    '''

    int_one = 1
    int_two = 2
    print("First integer:", int_one)
    print("Second integer:", int_two)
    print("Sum of integers =", int_one+int_two)

sum_integers()
