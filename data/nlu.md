version: "3.1"

nlu:
- intent: greet
  examples: |
    - hey
    - hello
    - hi
    - hello there
    - good morning
    - good evening
    - moin
    - hey there
    - let's go
    - hey dude
    - goodmorning
    - goodevening
    - good afternoon

- intent: goodbye
  examples: |
    - cu
    - good by
    - cee you later
    - good night
    - bye
    - goodbye
    - have a nice day
    - see you around
    - bye bye
    - see you later

- intent: affirm
  examples: |
    - yes
    - y
    - indeed
    - of course
    - that sounds good
    - correct

- intent: deny
  examples: |
    - no
    - n
    - never
    - I don't think so
    - don't like that
    - no way
    - not really

- intent: mood_great
  examples: |
    - perfect
    - great
    - amazing
    - feeling like a king
    - wonderful
    - I am feeling very good
    - I am great
    - I am amazing
    - I am going to save the world
    - super stoked
    - extremely good
    - so so perfect
    - so good
    - so perfect

- intent: mood_unhappy
  examples: |
    - my day was horrible
    - I am sad
    - I don't feel very well
    - I am disappointed
    - super sad
    - I'm so sad
    - sad
    - very sad
    - unhappy
    - not good
    - not very good
    - extremly sad
    - so saad
    - so sad

- intent: bot_challenge
  examples: |
    - are you a bot?
    - are you a human?
    - am I talking to a bot?
    - am I talking to a human?

- intent: ask_more_info
  examples: |
    - Can you tel me about your company?
    - what is all about your company?
    - what is your company doing?



- intent: request_diagnosis
  examples: |
    - diagnosis
    - Diagnosis
    - Check Vital Signs

- intent: vs_temperature
  examples: |
    - [temperature](vital_sign)
    - [Temp](vital_sign)
    - [Heat](vital_sign)
    - [pressure](vital_sign)
    - [Pressure](vital_sign)


- intent: vital_signs
  examples: |
    - i want to check [temperature](vital_sign)
    - i want to check [Temp](vital_sign)
    - i want to check [Heat](vital_sign)
    - i want to check [heart](vital_sign)
    - i want to check [Heart](vital_sign)
    - i want to check [all](vital_sign)
    - [all](vital_sign)
    - [respiration](vital_sign)
    - [Respiration](vital_sign)
#
#- intent: vs_pressure
#  examples: |
#    - [pressure](vital_sign)
#    - [Pressure](vital_sign)
#
#- intent: vs_heart
#  examples: |
#    - [heart](vital_sign)
#    - [Heart](vital_sign)
#
#- intent: vs_all
#  examples: |
#    - [all](vital_sign)
#    - [all](vital_sign)
#
#- intent: vs_respiration
#  examples: |
#    - [respiration](vital_sign)
#    - [Respiration](vital_sign)

- intent: prescription
  examples: |
    - prescription
    - Prescription
    - Treating the patient
    - prescribe the patient



- intent: give_time
  examples: |
    - can you tell me what time it is
    - tell me the time
    - got the time
    - what time is it

- intent: start
  examples: |
    - Lets get Started
    
