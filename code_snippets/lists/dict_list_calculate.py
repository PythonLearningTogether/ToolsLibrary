"""
Calculate the sum of all the dicts' amount in the following list.
"""
from functools import reduce

body = [
    {
        'amount': 120,
        'product': 1,
    },
    {
        'amount': 80,
        'product': 2,
    }
]

# 200
print(reduce(lambda x, y: {'amount': x['amount'] + y['amount']}, body)['amount'])

cal_total_amount = lambda iterable: reduce(lambda x, y: {'amount': x['amount'] + y['amount']}, iterable)['amount']

# 200
print(cal_total_amount(body))


# the reduct method above is faster than the following readable functional programming method
def calculate_sum(iterable):
    try:
        head = next(iterable)
        head_value = head['amount']
    except StopIteration:
        return 0
    return head_value + calculate_sum(iterable)


total_amount = calculate_sum(iter(body))
