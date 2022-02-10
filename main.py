import numpy


def valid_float(a):
    a_list = []
    char_count = 0
    for i in a:
        if i.isnumeric() or i in [" ", ",", "."]:
            if i.isnumeric():
                a_list.append(i)
            elif i == " ":
                continue
            elif i == ",":
                a_list.append(".")
                char_count += 1
            elif i == ".":
                a_list.append(i)
                char_count += 1
        else:
            return False
        if char_count == 2:
            return False
    return float("".join(a_list))


def valid_int(a):
    if not a.isnumeric():
        return False
    elif int(a) < 1:
        return False
    else:
        return int(a)


print("\n" + "-" * 50)
print("Welcome to BILL CALCULATOR!")
print("-" * 50)

bill_amount_input = input("\nWhat was the total bill amount? $")
while not valid_float(bill_amount_input):
    bill_amount_input = input("Invalid input. What was the total bill amount? $")
valid_bill_amount = valid_float(bill_amount_input)

percentage_input = input("\nWhat percentage tip would you like to give? %")
while not valid_float(percentage_input):
    percentage_input = input("Invalid input. What percentage tip would you like to give? %")
valid_percentage = valid_float(percentage_input)

people_count_input = input("\nHow many people to split the bill? ")
while not valid_int(people_count_input):
    people_count_input = input("Invalid input. How many people to split the bill? ")
valid_people_count = valid_int(people_count_input)

total_amount = valid_bill_amount * ((100 + valid_percentage) / 100)
amount_per_person = total_amount / valid_people_count

print("\nTotal amount is ${}".format(float(numpy.round(total_amount, 2))))
print("Each person should pay ${}".format(float(numpy.round(amount_per_person, 2))))