import markovgen

original = open("remezcla.txt", encoding='utf-8')
nuevo = open("mezclota.txt", "w", encoding="utf-8")

newtext = []

mk = markovgen.Markov(original)

counter = 0

while counter < 200:
    line = mk.generate_markov_text() + '\n'

    exclude = ['"', '(', ')', ';']
    line = ''.join(ch for ch in line if ch not in exclude)

    print(line)
    newtext.append(line)
    counter = counter + 1

for line in newtext:
    nuevo.write(line)
