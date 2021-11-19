try:
    number = int(input())
    assert number > 2
    for i in range(2, number - 1):
        assert number % i != 0
except AssertionError:
    print('This number is not prime')
else:
    print('This number is prime')
