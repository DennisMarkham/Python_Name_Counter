first_or_last = ""
def main():
  print("Type some names.  Write 'end' when you are finished")
  names = []
  new_name = ""
  while new_name != "end":
    new_name = input()
    names.append(new_name)


  desired_name = ""
  desired_name_count = 0





  def ask_first_or_last():
        global first_or_last
        first_or_last = input("Would you like to find a first name or last name \n")
        if first_or_last.strip() != "first" and first_or_last.strip() != "last":
            print("I don't understand, type first or last, please")
            ask_first_or_last()

  ask_first_or_last()

  desired_name = input("and what name would you like to find? \n")


  for x in names:
      seperated_names = x.rsplit(" ")
      if first_or_last.strip() == "last":
          last_name = seperated_names[len(seperated_names) - 1]
          if last_name == desired_name.strip():
              #global desired_name_count
              desired_name_count = desired_name_count + 1
      if first_or_last.strip() == "first":
          first_name = seperated_names[0]
          if first_name == desired_name.strip():
            #global desired_name_count
            desired_name_count = desired_name_count + 1
              
  print(desired_name_count)
  main()
main()

