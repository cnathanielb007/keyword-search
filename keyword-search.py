import wikipedia

while True:
  my_input = input("Keyword:- ")
  print(wikipedia.summary(my_input))
