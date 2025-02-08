print('-- begin --')

# Fill in the blanks to pass the assertions
number_of_eggs = 0

while number_of_eggs != 12:
    number_of_eggs = number_of_eggs + 1
    print('number_of_eggs:', number_of_eggs)

assert number_of_eggs == 12, 'there should be a dozen eggs'

print('-- end --')
