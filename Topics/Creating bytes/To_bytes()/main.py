number = int(input())
the_bytes = number.to_bytes(2, 'big')
print(sum(the_bytes))
