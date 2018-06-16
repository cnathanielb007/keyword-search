import wikipedia
import sys


while True:
  my_input = input("Keyword:- ")
#  my_input = sys.argv
  print(wikipedia.summary(my_input))
