percent100 = []
percent75 = []
percent50 = []
percent25 = []


def load_inventory(name):
    inv = []
    file_loaded = open(name + '.txt', 'r')
    for i in file_loaded:
        file_line = i.split(':')
        file_line[1] = int(file_line[1])
        if file_line[1] > 0:
            inv.append(file_line[0])
            inv.append(file_line[1])
    file_loaded.close()
    return inv


def check_recipe(name):
    file_loaded = open(name + '.txt', 'r')
    for i in file_loaded:
        file_line = i.split(':')
        recipe = []
        for j in file_line:
            if '\n' in j:
                j = j[:-1]
            if j.isnumeric() is True:
                recipe.append(int(j))
            else:
                recipe.append(j)
        recipe_rate(recipe, inventory)
    file_loaded.close()


def recipe_rate(rec, inv):
    rate = 0
    for i in range(1, len(rec), 2):
        for j in range(0, len(inv), 2):
            if inv[j] == rec[i]:
                count_temp = inv[j+1]
                while count_temp > 0 and rec[i+1] > 0:
                    rec[i+1] -= 1
                    count_temp -= 1
                    rate += 1
    if rate >= 4:
        percent100.append(rec[0])
    elif rate == 3:
        percent75.append(rec[0])
    elif rate == 2:
        percent50.append(rec[0])
    elif rate == 1:
        percent25.append(rec[0])


def printlist():
    print('lista dos 100%')
    for i in percent100:
        print(i)
    print('lista dos 75%')
    for i in percent75:
        print(i)
    print('lista dos 50%')
    for i in percent50:
        print(i)
    print('lista dos 25%')
    for i in percent25:
        print(i)


print('Carregando itens...')
inventory = load_inventory('inventory')
print('itens carregados!')
print('Validando as receitas...')
check_recipe('reciperead')
print('Validação concluída!!!')
print('Imprimindo lista:')
printlist()
