import random

name = ""
question = "Should I learn Computer Science?"
answer = ""

random_number = random.randint(1, 12)

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "I don't see why not"
elif random_number == 11:
  answer = "I can't tell you yet"
elif random_number == 12:
  answer = "Do what you must"
else:
  answer = "Error"

if question == "":
  print("Please ask a question of the 8-Ball otherwise the fabric of reality is at risk.")
else:
  if name == "":
    print("Question: " + question)
    print("Magic 8-Ball's answer: " + answer + ".")
  else:
    print(name + " asks: " + question)
    print("magic 8-Ball's answer: " + answer + ".")
