print("Hello,today you are going to answer some questions to determine whats your spirit animal!")
print('Press enter if you would like to continue....')
input()
animal_cheetah = 0
animal_fish = 0
animal_bird = 0 
animal_bear = 0 

answer1 = input("Would you rather A run quickly, B swim fast, C be able to levitate or be D super strong? (Answer in uppercase): ")
if answer1 == "A":
    animal_cheetah += 1
elif answer1 == "B":
    animal_fish += 1
elif answer1 == "C":
    animal_bird+= 1
elif answer1 == "D":
    animal_bear += 1
answer2 = input("Where would you rather live? A:Savanna with many animals,B:Beach house near the ocean,C:Tropical rainforest, D:Snowy mountains?(Answer in uppercase): ")
if answer2 == "A":
    animal_cheetah += 1
elif answer2 == "B":
    animal_fish += 1
elif answer2 == "C":
    animal_bird+= 1
elif answer2 == "D":
    animal_bear += 1
answer3 = input("How would you rather spend your time? A:Going on a hike,B:Going on a swim,C:Going parachuting,D:Going skiing (Answer in uppercase): ")
if answer3 == "A":
    animal_cheetah += 1
elif answer3 == "B":
    animal_fish += 1
elif answer3 == "C":
    animal_bird+= 1
elif answer3 == "D":
    animal_bear += 1
    answer3 = input("Whats your favorite season?A:Summer,B:Fall,C:Winter,D:Spring(Answer in uppercase): ")
if answer3 == "A":
    animal_cheetah += 1
elif answer3 == "B":
    animal_fish += 1
elif answer3 == "D":
    animal_bird+= 1
elif answer3 == "C"or"A":
    animal_bear += 1
answer4 = input("How would your friends describe you? A:Curious, B:shy, C:intelligent(Answer in uppercase): ")
if answer4 == "A":
    animal_cheetah += 1 
    animal_bird+= 1
elif answer4 == "B":
    animal_fish += 1
elif answer4 == "C"or"B":
    animal_bear += 1
if animal_cheetah >= animal_bird and animal_cheetah >= animal_fish and animal_cheetah>=animal_bear:
        print("Your spirit animal is a cheetah!")
        print("Cheetahs are speedy and efficient, capable of moving quickly through challenges and getting things done without unnecessary delay")
if animal_fish >= animal_cheetah and animal_fish>= animal_bear and animal_fish >= animal_bird:
        print("Your spirit animal is a fish!")
        print("Fishes are known for adaptability, intuition, emotional depth, and tranquility")
if animal_bird >= animal_bear and animal_bird>= animal_cheetah and animal_bird>= animal_fish:
        print("Your spirit animal is a bird ")
        print("Birds are known for boldness or exploratory behavior ")
if animal_bear>=animal_bird and animal_bear>= animal_cheetah and animal_bear >=animal_fish:
        print("Your spirit animal is a bear")
        print("People with a bear personality are often grounded, powerful, and fiercely loyal ")



