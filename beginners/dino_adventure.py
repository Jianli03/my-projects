name = input("Type your name: ")
print("Welcome", name, "to the Whispering Woods!")

print("You're exploring the forest when you hear a loud rustle in the bushes. A small green dinosaur with big, curious eyes pops out!")

answer = input("Do you want to (a) approach the dinosaur or (b) hide behind a tree? ").lower()

if answer == "a":
  print("The dinosaur cautiously approaches you. It seems friendly!")
  answer = input("Do you want to (a) offer it some of your berries or (b) pet its head? ").lower()
  if answer == "a":
    print("The dinosaur happily nibbles on your berries. It seems grateful!")
    answer = input("Would you like to (a) ask the dinosaur to play or (b) follow it deeper into the forest? ").lower()
    if answer == "a":
      print("The dinosaur chases butterflies with you, and you have a wonderful time playing together. You win!")
    elif answer == "b":
      print("The dinosaur leads you to a hidden waterfall and a secret grove full of delicious berries. You win!")
    else:
      print("Invalid choice. You lose your chance to explore with the friendly dino!")
  elif answer == "b":
    print("The dinosaur feels threatened and lets out a loud bellow. You scare it away. You lose!")
  else:
    print("Invalid choice. The dinosaur is confused and wanders off. You miss your chance to befriend it!")
elif answer == "b":
  print("The dinosaur sniffs around but doesn't see you. It wanders off.")
  answer = input("Do you want to (a) peek out from behind the tree or (b) stay hidden? ").lower()
  if answer == "a":
    print("You see the dinosaur is friendly and eating leaves peacefully. You regret hiding!")
  elif answer == "b":
    print("You stay hidden for a while, then decide it's safe to come out. The dinosaur is gone. You miss your chance to meet it!")
  else:
    print("Invalid choice. You stay hidden for too long and miss your chance to see the dinosaur!")
else:
  print("Invalid choice. You panic and run away, scaring the dinosaur. You lose!")

print("Thank you for exploring the Whispering Woods with", name, "!")