# Imports
import random as r
from time import sleep, time
from Win import winner


# Player attributes
class Player():
    def __init__(self, lives):
        self.lives = lives

    def lose_life(lives):
          lives -= 1
          #heart emoji
          number_of_hearts = "\u2764\ufe0f"*lives
          print(f"Lives Left: {lives} {number_of_hearts}")
          print("-------------------------------------------")
          return lives
        

# Questions
class Questions():
    def qList():
        question_list = [Questions.q1(), Questions.q2(),Questions.q3(), Questions.q4(),Questions.q5()]
        # print(question_list)
        return question_list

    def q1():
        hints = Hints.set_1()
        answer = 'dog'
        short_description = "\U0001F415 Dog is the best friend of man. In total, there is said to be around 400 million dogs worldwide."

        return answer, hints, short_description

    def q2():
        hints = Hints.set_2()
        answer = 'cat'
        short_description = "\U0001F408 Cats can jump up to 6 times their height. They are also known to always fall on their feet, no matter what height they jump from."
        return answer, hints, short_description

    def q3():
        hints = Hints.set_3()
        answer = 'elephant'
        short_description = "\U0001F418 Elephants cannot jump and spend around 16 hours eating daily. Their lifespan is around 70 years. "
        return answer, hints, short_description

    def q4():
        hints = Hints.set_4()
        answer = 'giraffe'
        short_description = "\U0001F992  A giraffe's heart is two feet long. The males are called 'Bulls', the females are called 'Cows' and the kids are called 'Calves'."
        return answer, hints, short_description

    def q5():
        hints = Hints.set_5()
        answer = 'lion'
        short_description = "\U0001F981 Female lions are the main hunters of the pride (group of lions). They are nocturnal hunters."
        return answer, hints, short_description


# Hint attributes
class Hints():
    def __init__(self):
        pass

    # Hints for Questions in list
    def set_1():
        hint = ['Cerberus', "Inverted 'god'", "Man's best friend"]
        return hint

    def set_2():
        hint = ['Has 18 toes in total', '9 lives', 'Always lands on its feet']
        return hint

    def set_3():
        hint = ['Namesake of Ivorine', 'Afraid of mice', 'Never forgets']
        return hint

    def set_4():
        hint = ['Drops their babies from 1.5m when giving birth', 'Only needs to sleep 5-30mins within 24hrs', 'Long neck']
        return hint

    def set_5():
        hint = ['The only cats that live in groups', 'Males have magnificent facial hair, also known as mane', 'King of the jungle']
        return hint
      
    # gives hint + add 1 to counter
    def provide_hint(hint_set, hint_counter):
        print("Hint: " + hint_set[hint_counter])
        hint_counter += 1
        return hint_counter



class GamePlay():
    def __init__(self):
      #prompt for name
      name = input("Hi player, what's your name?")
      #player start with 3 lives
      player = Player(3)
      self.replay = True
      qList = Questions.qList()

      #heart emoji
      initial_hearts = "\u2764\ufe0f"*3

      #introduction to game
      print(f"Hi {name}, welcome to Anivia! \U0001F60A \nYou'll have to guess the animal based on the hints given that will describe the animals.\nOne life will be deducted for every question that you answered wrongly (Don't worry, each question have 3 attempts without live deduction and 3 different hints will be provided~).\nIt's game over once all lives are used up.\nLet's get the game started! \U0001F609 \nYou have {player.lives} lives. {initial_hearts}")
      sleep(2)

      #start timing for overall
      start_time = time()
      
      #some for loop here, coding later
      try:
        while player.lives > 0 and self.replay == True:
          #randomising question
          question_number = r.randint(0,len(qList)-1)
          question = qList.pop(question_number)
          hint_counter = 0

          #setting up the empty blanks for hints
          blanks = list('_'*len(question[0]))
          
          # Question Starts
          print(f'\nGuess this animal!\nLetter: {len(question[0])}\nYou have 20 seconds to answer!')

          #original working code, DO NOT DELETE
          # while hint_counter < 3 and '_' in blanks:
          #   hint_counter = Hints.provide_hint(question[1],hint_counter)
          #   print(" ".join(blanks))
          #   #getting input
          #   player_answer = input("Answer: ")
          #   # Convert Lowercase
          #   player_answer = player_answer.lower()
          #   blanks = GamePlay.check_answer(question[0],player_answer,blanks)
          # time_taken = round((time() - e_question_start),2)

          #timer implemented, does not affect students as much who does not answer (leaving input blank)
          e_question_start = time()

          while hint_counter < 3 and '_' in blanks and (time()-e_question_start) <= 20:
            hint_counter = Hints.provide_hint(question[1],hint_counter)
            print(" ".join(blanks))
            #getting input
            player_answer = input("Answer: ")

            # Convert Lowercase
            player_answer = player_answer.replace(" ", "").lower()
            blanks = GamePlay.check_answer(question[0],player_answer,blanks)
          

          #getting total time taken for the question
          time_taken = round((time() - e_question_start),2)

          #converting seconds to h:mm:ss
          seconds = time_taken % (24 * 3600)
          hour = seconds // 3600
          seconds %= 3600
          minutes = seconds // 60
          seconds %= 60

          # Check success
          if '_' in blanks:
            print(f"The answer was {question[0]}!")
            print("%d:%02d:%02d" % (hour, minutes, seconds))
            player.lives = Player.lose_life(player.lives)   
          else:
            print(f"Correct. The answer is {question[0]}! \U0001f600")
            print(f"More about {question[0]}:\n{question[2]}")
            print("Time taken: " + "%d:%02d:%02d" % (hour, minutes, seconds))
            print("-------------------------------------------")
            pass     
          
          # Game Over
          if player.lives == 0:
            print(f"Game Over!\nDon't give up {name}!")

            # fail-safe loop break
            self.replay = False

          # Replay? (scrapped)
          
          # All questions Complete
          if len(qList) == 0:
            #getting time and converting it
            gameplay_time = time() - start_time
            seconds = gameplay_time % (24 * 3600)
            hour = seconds // 3600
            seconds %= 3600
            minutes = seconds // 60
            seconds %= 60

            #output for winning
            print("You have completed the game! Hope you learnt some animal knowledge from this trivia~ \U0001F929")
            # print("%d:%02d:%02d" % (hour, minutes, seconds))

            #getting stars for timing 
            if(gameplay_time < 30):
              print("\U0001F31F"*3)
            elif(gameplay_time >= 30 and gameplay_time < 50): 
              print("\U0001F31F"*2)
            elif(gameplay_time >= 50 and gameplay_time < 80):
              print("\U0001F31F"*1)
            else:
              print("You have no stars")            

            #surprise drawing for the winner
            winner()
            
            # fail-safe loop break
            self.replay = False
            break

          # Delay (Quality of Life)
          sleep(1)
          continue
      # Force Stop upon Ctrl+C
      except KeyboardInterrupt:
          print("Program has been force stopped")


    def check_answer(answer, player_input, display):
        # To ensure within index (Fool proof, original code)
        # check = answer if len(answer) <= len(player_input) else player_input
        # compare = player_input if len(answer) <= len(player_input) else answer
        
        # To ensure within index (Fool proof)
        if(len(answer) <= len(player_input)):
          check = answer
          compare = player_input
        else:
          check = player_input
          compare = answer
        
        for index, letter in enumerate(check):
          # check answer correct
          if letter == compare[index]:
            #replace display
            display[index] = letter
        return display
