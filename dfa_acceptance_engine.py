import sys

f = open(sys.argv[1], "r")
word = sys.argv[2]
# f = open('dfa_config_file1.in', 'r')
# word = input("Cuvant: ")

lsw = []
sigma = []
states = []
transitions = []
temp = []

# bagam cuvantul sub forma de lista de litere

for x in word:
    lsw.append(x)

# retinem alfabetul, starile si tranzitiile in liste

for line in f:
    line.strip()
    if line[0] == '#':
        continue
    else:
        line = line.rstrip('\n')
        temporary = line.split('#')
        temp = temporary[0].rstrip()
        temp = temp.split()
        if temp[0].lower().startswith('sigma'):
            Sigma = True
            temp.clear()
            for lineSigma in f:
                lineSigma = lineSigma.strip('\n')
                lineSigma = lineSigma.strip()
                temporary = lineSigma.split('#')
                lineSigma = temporary[0].rstrip()
                if lineSigma.lower().startswith('end'):
                    break
                if len(lineSigma) != 0:
                    sigma.append(lineSigma)

        elif temp[0].lower().startswith('states'):
            States = True
            temp.clear()
            for lineStates in f:
                lineStates = lineStates.rstrip("\n")
                lineStates = lineStates.strip()
                temporary = lineStates.split('#')
                lineStates = temporary[0].rstrip()
                if lineStates.lower().startswith('end'):
                    break
                if len(lineStates) != 0:
                    states.append(lineStates.split())
            for ls in states:
                ls[0] = ls[0].rstrip(",")
                if len(ls) == 3:
                    ls[1] = ls[1].rstrip(",")

        elif temp[0].lower().startswith('transitions'):
            Transitions = True
            temp.clear()
            for lineTransitions in f:
                lineTransitions = lineTransitions.rstrip("\n")
                lineTransitions = lineTransitions.strip()
                temporary = lineTransitions.split('#')
                lineTransitions = temporary[0].rstrip()
                if lineTransitions.lower().startswith('end'):
                    break
                if len(lineTransitions) != 0:
                    transitions.append(lineTransitions.split())
            for ls in transitions:
                ls[0] = ls[0].rstrip(",")
                ls[1] = ls[1].rstrip(",")

finals = []

# facem lista pentru toate starile finale si o variabila pentru starea de start

for state in states:
    if len(state) == 2 and state[1] == "S":
        start = state[0]
    if len(state) == 2 and state[1] == "F":
        finals.append(state[0])
    if len(state) == 3 and state[1] == "S" and state[2] == "F":
        finals.append(state[0])
        start = state[0]
    elif len(state) == 3 and state[1] == "F" and state[2] == "S":
        finals.append(state[0])
        start = state[0]

# verificam acceptarea cuvantului, folosind fiecare litera a cuvantului in ordine o singura data, apoi stergand-o din lista.

rn = start
while len(lsw)!=0:
    good = False
    if lsw[0] in sigma:
        for transition in transitions:
            if transition[0] == rn and transition[1] == lsw[0]:
                rn = transition[2]
                good = True
                break
        if good == False:
            print("Not accepted!")
            exit(0)
    else:
        print("Not good")
        exit(0)
    if len(lsw) == 1:
        lsw.clear()
    else:
        lsw = lsw[1:]

if good == True and rn in finals:
    print("ACCEPTED")
else:
    print("NOT ACCEPTED")
f.close()