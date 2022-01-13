# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 15:33:02 2021

@author: user
"""

# import nltk
import random
import ast



def Read_file_as_dictionary(fname):
    file = open(fname,'r')
    contents = file.read()
    dictionary = ast.literal_eval(contents)
    file.close()
    return dictionary


def User_input_processing(input_str):
    punct_list = [",", ".", "!", "?", "'", '"', "/", ";", ":"]
    input_str = input_str.lower()
    for i in range(len(punct_list)):
        input_str = input_str.replace(punct_list[i], " ")
    input_list = input_str.split(" ")
    while "" in input_list:
        input_list.remove("")
    return input_list
    

def Generate_response(response_intent, intents_dict):    

    response = None
    for intent in intents_dict["intents"]:
        if intent['tag'] == response_intent:
            response = random.choice(intent["responses"])
    return response


def Input_classification(user_input, intents_dict):
    intent_score_list = []
    for intent in intents_dict['intents']:
        score = 0
        for i in range(len(user_input)):
            for pattern in intent['major patterns']:
                if pattern == user_input[i]:
                    score = score + 10
            for pattern in intent['minor patterns']:
                if pattern == user_input[i]:
                    score = score + 1       
        intent_score_list.append(score)
        
    max_score = max(intent_score_list)
    num_max = intent_score_list.index(max_score)
    intent_input = intents_dict['intents'][num_max]['tag']
    return intent_input, max_score




intents_dict = Read_file_as_dictionary('intents.txt')

robo_responce = Generate_response("greeting", intents_dict)
print(robo_responce, end='')

while True:
    user_input = input()
    user_input_final = User_input_processing(user_input)
    user_intent, score = Input_classification(user_input_final, intents_dict)
    
    if score<2:
        robo_responce = Generate_response("end conversation", intents_dict)
        print(robo_responce, end='')

    elif user_intent == "goodbye":
        robo_responce = Generate_response("goodbye", intents_dict)
        print(robo_responce, end='')
        break

    else :
        robo_responce = Generate_response(user_intent, intents_dict)
        print(robo_responce, end='')
