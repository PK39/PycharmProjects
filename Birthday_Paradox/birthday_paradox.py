"""Birthday paradox Simulation
Exploring probabilities of the birthday paradox."""

import datetime, random


def getBirthdays(numberOfBirthdays):
    """Returns list of birthdazs (random)"""
    birthdays = []
    for i in range(numberOfBirthdays):
        # year unimportant for simulation, as long as all
        # birthdays have the same year.
        startOfYear = datetime.date(2001, 1, 1)

        # Get a random day into the year:
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None

    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1]):
            if birthdayA == birthdayB:
                return birthdayA

print('''Birthday Paradox\n
    The Birthday Paradox shows us that in a group of N people, the odds
    that two of them have matching birthdays is actually surprisingly large.
    This program does a Monte Carlo simulation (that is, repeated random
    simulations) to explore this concept.
    \n
    (It's not actually a pradox, its just a surprising result.)''')

MONTHS = ('January ', 'Feb ', 'Mar ', 'Apr ', 'May ', 'Jun ',
          'Jul ', 'Aug ', 'Sep ', 'Oct ', 'Nov ', 'Dec ')

while True:
    print('How many birthdays shall I generate (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int (response) <= 200):
        numBDays = int(response)
        break

print('Here are', numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{}{}'.format(monthName, birthday)
    print(dateText, end='')

match = getMatch(birthdays)

print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{}{}'.format(monthName, match.day)
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays.')
print()


print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations.')
simMatch = 0
for i in range(100_000):
    if i % 1000 == 0:
        print(i, 'simulations run...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100,000 simulations run.')

probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a mtaching birthday in their group.')
print('That\'s probably more than you would think!')
