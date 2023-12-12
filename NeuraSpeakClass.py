import nltk
import language_tool_python
import numpy as np
import speech_recognition as sr
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
import random
import nltk

class NeuraSpeakAssistant:
    def __init__(self):
        # Inicialize recognizer
        self.r = sr.Recognizer()

    # Funtion to recognize audio of the user
    def recognize_speech(self):
        with sr.Microphone() as source:
            print("Speak now...\n")
            audio = self.r.listen(source)
            try:
                text = self.r.recognize_google(audio)
                print("You try to said: " + text)
                return text
            except sr.UnknownValueError:
                print("Sorry, I could not understand what you said.")
                return ""
            except sr.RequestError as e:
                print("Could not request results from Speech Recognition service; {0}".format(e))
                return ""

    # Funtion to detect errors and suggest corrections
    def recognize_errors(self, text):
        tokens = word_tokenize(text)
        print(f"Tokens: {tokens}")
        pos_tags = nltk.pos_tag(tokens)
        print(f"Tokens tag: {pos_tags}")
        # set of the language
        tool = language_tool_python.LanguageTool('en-US')
        matches = tool.check(text)
        len(matches)
        for i in matches:
            print(i)
        corrected_text = tool.correct(text)
        return corrected_text

    # Function to practice vocabulary
    def practice_vocabulary_quiz(self):
        while True:
            words = []
            definitions = []
            # Wordnet set
            for synset in wordnet.all_synsets('n'):
                words.append(synset.name().split(".")[0])
                definitions.append(synset.definition())
                
            quiz_words = random.sample(words, k=4)
            correct_word = random.choice(quiz_words)
            print("==========================================================")
            print("What is the definition of the following word?")
            print(correct_word)
        
            for i in range(len(quiz_words)):
                print(f"{i + 1}. {definitions[words.index(quiz_words[i])]}")
            
            answer = input("Enter the correct option number: ")
    
            if not answer.isdigit() or int(answer) not in range(1, 5):
                print("==========================================================")
                print("Invalid response. Please enter a valid number between 1 and 4.")
                continue

            if int(answer) == quiz_words.index(correct_word) + 1:
                print("==========================================================")
                print("Congratulations! Your answer is correct.")
            else:
                print(f"Sorry, your answer is incorrect. The correct answer is {quiz_words.index(correct_word) + 1}.")

            play_again = input("Do you want to practice again? (y/n): ").lower()
            if play_again != 'y':
                break

    # Function to generate quiz practice
    def generate_vocabulary_quiz(self, num_questions):
        words = []
        definitions = []
        score = 0

        # 
        for synset in wordnet.all_synsets('v'):
            if synset.pos() == "v":
                words.append(synset.name().split(".")[0])
                definitions.append(synset.definition())

        for i in range(num_questions):
            quiz_words = np.random.choice(words, size=4, replace=False)
            correct_word = np.random.choice(quiz_words)

            print(f"\nQuestion {i + 1}: What is the definition of the following word?")
            print(correct_word)

            for j in range(len(quiz_words)):
                print(f"{j + 1}. {definitions[words.index(quiz_words[j])]}")

            answer = int(input("Enter the correct option number: "))

            if answer == np.where(quiz_words == correct_word)[0][0] + 1:
                print("Congratulations! Your answer is correct.")
                score += 1
            else:
                print(f"Sorry, your answer is incorrect. The correct answer is {np.where(quiz_words == correct_word)[0][0] + 1}.")

        # score
        print(f"\nQuiz complete! Your score is: {score}/{num_questions}")

    # Menu function
    def start_voice_assistant(self):
        print("_________________________________________________")
        print("*** Welcome to the NeuraSpeak Voice Assistant ***")
        print("_________________________________________________")
        while True:
            print("\nWhat would you like to do?\n")
            print("1. Recognize pronunciation errors and suggest corrections")
            print("2. Practice vocabulary")
            print("3. Quiz")
            print("4. Exit")
            print("_________________________________________________")
            choice = input("Enter your choice: ")

            if choice == "1":
                text = self.recognize_speech()
                if text:
                    corrected_text = self.recognize_errors(text)
                    print(f"Corrected text: {corrected_text}")
            elif choice == "2":
                self.practice_vocabulary_quiz()
            elif choice == "3":
                self.generate_vocabulary_quiz(10)
            elif choice == "4":
                print("Thank you for using the NeuraSpeak learning voice assistant.")
                break
            else:
                print("Invalid choice. Please try again.")

#assistant = NeuraSpeakAssistant()
#assistant.start_voice_assistant()