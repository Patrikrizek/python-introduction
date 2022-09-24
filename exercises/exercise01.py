def exercise_one():
  name = 'Patrik'
  surname = 'Smith'
  fullname = name + ' ' + surname
  name_to_array = 'Patrik,Smith'
  example = '    This is a simple text    '
  current_year = 2022
  year_txt = 'Current Year is: {}'

  print(fullname)
  print(name.upper() + ' ' + surname.lower())
  print(len(fullname))
  print(example.strip())
  print(name.replace('Patrik', 'John'))
  print(name_to_array.split(','))
  print(year_txt.format(current_year))

exercise_one()  