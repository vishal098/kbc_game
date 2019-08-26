
# import pyttsx3
# engine=pyttsx3.init()
# engine.setProperty('volume',10)
# engine.setProperty('rate',100)
# a=0
# while a<10:
# 	user=input("write anything:\n")
# 	engine.say(user)
# 	engine.runAndWait()
# 	a+=1


import pyttsx3
engine=pyttsx3.init()
engine.setProperty('volume',1)
engine.setProperty('rate',150)
print("welcome to  kbc game!!!")
engine.say("welcome to  kbc game")
engine.runAndWait()
print()
engine.say("what is your name")
engine.runAndWait()
name=input("what is your name: ")
print()
print("hello ",name,"......\n")
engine.say("hello")
engine.say(name)
engine.say("welcome in the games")
engine.runAndWait()
engine.say("would u like to begin the game")
engine.runAndWait()
b=0
while b<1:
	user=input("would u like to begin: ")
	if user=="yes":
		print()
		print("your game has begin")
		engine.say("your game has begin")
		engine.runAndWait()
		print()
	elif user=="no":
		print()
		print("Thanks for trying the game, Goodbye :")
		engine.say("Thanks for trying the game, Goodbye")
		engine.runAndWait()		
		break
	else:
		print()
		print("you choose improper word")
		engine.say("you choose improper word")
		engine.runAndWait()		
		break	
	questions=[
				"What is the capital of Russia?",
				"How many states are there in America?",
				"What is the currency of France?",
				"When were the first recorded Olympics held?",
				"The team Beamer is associated with?",
				"Of which country is bull-fighting the national game?"
				]
	options=[
				["1.) London","2.) Tibet","3.) Mosco","4.) Ottawa"],
				["1.) 34","2.) 23","3.) 46","4.) 50"],
				["1.) Dollar","2.) Euro","3.) Renminbi","4.) Yemeni rial"],
				["1.)825 BC","2.)776 BC","3.)320 BC","4.)80 AD"],
				["1.)Football","2.)Hockey","3.)Cricket","4.)Chess"],
				["1.)Spain","2.)Portugal","3.)Hungary","4.)Poland"]
				]
	answer=[3,4,2,2,3,1]
	money=[5000,10000,20000,40000,80000,160000]			
	a=0
	for i in questions:
		print("your",a+1,"question is....","\n")
		engine.say("your")
		engine.runAndWait()
		engine.say(a+1)
		engine.runAndWait()
		engine.say("question is")
		engine.runAndWait()
		print(questions[a])
		engine.say(questions[a])
		engine.runAndWait()
		for j in (options[a]):
			print(j)
			engine.say(j)
			engine.runAndWait()
		print()
		engine.say("write your answer")
		engine.runAndWait()		
		user=input("answer: ")
		print()

		list1=["1","2","3","4"]
		if user not in list1:
			print("your answer is not in options")
			engine.say("your answer is not in options")
			engine.runAndWait()	
			break
		elif int(user)==int(answer[a]):
			print("your answer is correct","\n")
			engine.say("congratulations your answer is correct")
			engine.runAndWait()
			a+=1
		else:
			print("your answer is incorrect","\n")
			engine.say("sorry your answer is incorrect")
			engine.runAndWait()	
			break
			print()
	print("Thanks for playing the game")
	engine.say("Thanks for playing the game")
	engine.runAndWait()		
	b+=1
	






		