from boggle_board import BoggleBoard
import sys

boggle = BoggleBoard()

while (True):
  choice = input("S! for shake, P! for print or word\n")
  if choice == "S!":
      boggle.shake()
      print("Board has been shaken up")
  elif choice == "P!":
      boggle.print_board()
  elif choice == "exit()":
      print("Goodbye!")
      break
  else:
      print(f"Board includes {choice.upper()}: {boggle.include_word(choice)}")
  print()