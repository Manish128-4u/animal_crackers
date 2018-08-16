def animal_crackers(animal):
    word_list = animal.split()
    first_word = word_list[0]
    second_word = word_list[1]

    if first_word[0] == second_word[0]:
      print "True"
    else:
      print "False"

animal_crackers('ant eater')
