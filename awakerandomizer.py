import random
awakeclasses = open('awakeclasses.txt', 'r')
awakegrowths = open('awakegrowths.txt', 'r')

classes = []
chardict = {}

for line in awakeclasses:
    classes.append(line)

for line in awakegrowths:
    line = line.split()
    chardict[line[0]] = [int(i) for i in line[1:7]]
    
hasDancer = False

def randomize(character):
    charclass = random.choice(classes)
    total = sum(chardict[character])
    stats = [0,0,0,0,0,0,0,0]
    while max(sum(stats)-total, total-sum(stats)) > 10:
        for i in range(8):
            stats[i] = random.randint(25, 110)
    return '''
{}
Class: {}
HP: {}%
STR: {}%
MAG: {}%
SKL: {}%
SPD: {}%
LCK: {}%
DEF: {}%
RES: {}%
'''.format(character, charclass, stats[0], stats[1], stats[2], stats[3], stats[4], stats[5], stats[6], stats[7])

for character in chardict:
    print(randomize(character))
