import random

bday_messages = ['Hope you have a very Happy Birthday! 🎈',
'It\'s your special day – get out there and celebrate! 🎉',
'You were born and the world got better – everybody wins! 🥳',
'Have lots of fun on your special day! 🎂',
'Another year of you going around the sun! 🌞']

num = random.randint(1, 5)

if num == 1:
    random_message = 'Hope you have a very Happy Birthday! 🎈'
elif num == 2:
    random_message = 'It\'s your special day – get out there and celebrate! 🎉'
elif num == 3:
    random_message = 'You were born and the world got better – everybody wins! 🥳'
elif num == 4:
    random_message = 'Have lots of fun on your special day! 🎂'
else:
    random_message = 'Another year of you going around the sun! 🌞'