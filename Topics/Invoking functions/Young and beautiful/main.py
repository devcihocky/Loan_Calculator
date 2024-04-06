jack_age = int(input())
alex_age = int(input())
lana_age = int(input())

# if jack_age < alex_age and jack_age < lana_age:
#     print(int(jack_age))
# elif alex_age < jack_age and alex_age < lana_age:
#     print(int(alex_age))
# elif lana_age < jack_age and lana_age < alex_age:
#     print(int(lana_age))

print(min(jack_age, alex_age, lana_age))
