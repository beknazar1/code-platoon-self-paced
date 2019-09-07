def fizzbuzz():
    OUTPUT = []
    for index in range(1, 101):
        line = ''
        if index % 3 == 0 :
            line += 'fizz'
        if index % 5 == 0 :
            line += 'buzz'
        OUTPUT.append(index if line == '' else line.capitalize())

    return OUTPUT