in_message = input()
in_key = int(input())

key = sum(i for i in in_key.to_bytes(2, 'big'))
print(''.join(chr(ord(i) + key) for i in in_message))
