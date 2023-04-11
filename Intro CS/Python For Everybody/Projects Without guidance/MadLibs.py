import art
import random
from time import sleep

Nouns = []
Places = []
Occupation = []
Numbers = []
Verbs = []
BodyParts = []
Adjectives = []

while len(Nouns) < 5:
    Nouns = input(
        'Please Enter 5 or more Nouns (Separate between them with spaces):- ')
    Nouns = Nouns.rstrip()
    Nouns = Nouns.rsplit(' ')
    if len(Nouns) < 5:
        print('insufficient entries.')
        sleep(2)
while len(Places) < 2:
    Places = input(
        'Please Enter 2 or more Place ( Separate between them with spaces):- ')
    Places = Places.rstrip()
    Places = Places.rsplit(' ')
    if len(Places) < 2:
        print('insufficient entries')
while len(Occupation) < 2:
    Occupation = input(
        'Please Enter 2 or more occupations (Separate between them with spaces):- ')
    Occupation = Occupation.rstrip()
    Occupation = Occupation.rsplit(' ')
    if len(Occupation) < 2:
        print('insufficient entries')
while len(Numbers) < 2:
    Numbers = input(
        'Please Enter 2 or more Numbers (Separate between them with spaces):- ')
    Numbers = Numbers.rstrip()
    Numbers = Numbers.rsplit(' ')
    if len(Numbers) < 2:
        print('insufficient entries')
while len(Verbs) < 3:
    Verbs = input(
        'Please Enter 3 or more Verbs Ending with ING (Separate between them with spaces):- ')
    Verbs = Verbs.rstrip()
    Verbs = Verbs.rsplit(' ')
    if len(Verbs) < 3:
        print('insufficient entries')
while len(BodyParts) < 2:
    BodyParts = input(
        'Please Enter 2 or more body parts (Separate between them with spaces):- ')
    BodyParts = BodyParts.rstrip()
    BodyParts = BodyParts.rsplit(' ')
    if len(BodyParts) < 2:
        print('insufficient entries')
while len(Adjectives) < 4:
    Adjectives = input(
        'Please Enter 4 or more adjectives (Separate Between them with spaces):- ')
    Adjectives = Adjectives.rstrip()
    Adjectives = Adjectives.rsplit(' ')
    if len(Adjectives) < 4:
        print('insufficient entries')

print('Hello, my fellow ' + random.choice(Nouns) +
      's in 2023, it\'s me George Washington,')
sleep(0.8)
print('the first ' + random.choice(Occupation) +
      '. Iam writing from the ' + random.choice(Places) + ' ,Where')
sleep(0.8)
print('I have been secretly living living for the past ' +
      random.choice(Numbers) + ' years. I am')
sleep(0.8)
print('concerned by the ' + random.choice(Adjectives) +
      ' state of affairs in America this days.')
sleep(0.8)
print('It seems that your politicians are more concerned with ' +
      random.choice(Verbs) + 'ing one another than listining to the')
sleep(0.8)
print(random.choice(Nouns)+'s of the people. When we declared our independence')
sleep(0.8)
print('from the ' + random.choice(Places) +
      ', we set forth on a/an ' + random.choice(Adjectives) + ' path')
sleep(0.8)
print('guided by the voices of the everydays ' +
      random.choice(Nouns) + 's. if we\'re going to')
sleep(0.8)
print('keep ' + random.choice(Verbs) +
      'ing, then we need to learn how to respect all')
sleep(0.8)
print(random.choice(Nouns) + 's. Don\'t get me wrong; we had ' +
      random.choice(Adjectives) + ' problems')
sleep(0.8)
print('in my day, too. Benjamin Franklin once called me a/an ' + random.choice(Nouns))
sleep(0.8)
print('and kicked me in the ' + random.choice(BodyParts) +
      '. But at the end of the day, we')
sleep(0.8)
print('were able to ' + random.choice(Verbs) +
      ' in harmony. Let us find that ' + random.choice(Adjectives))
sleep(0.8)
print('spirit once again, or else I\'m taking my ' +
      random.choice(BodyParts) + ' off the quarter')
