def is_phone_valid(phone):
  if len(phone) != 12 or phone[3] != '-' or phone[7] != '-':
      return False
  for i in range(0, 12):
      if i != 3 and i != 7 and phone[i].isdigit() == False:
          return False
  return True


def is_email_valid(email):
    at_count = 0
    dot_count = 0
    for character in email:
        if character == '@':
            at_count += 1
        if character == '.':
            dot_count += 1
    return at_count == 1 and dot_count >= 1

def main():
    print("Welcome to the sign-up form.")
    print("Please provide your email and phone number so we can contact you.")

    number = input("Phone number: ")
    address = input("Email Address: ")


    number_valid = is_phone_valid(number)
    address_valid = is_email_valid(address)

    if number_valid and address_valid:
        print("Thanks for providing your information")
    else:
        print("Something is not right. Please try again.")

main()