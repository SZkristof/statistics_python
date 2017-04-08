def get_most_played(file_name):
    with open(file_name) as file:

        data_list = file.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        list_of_money = [data_list[i][int(1)] for i in range(len(data_list))]  # append 1st part to list in range of 2nd
        list_of_money = [float(i) for i in list_of_money]
        highest_value = max(list_of_money)
        place_of_value = [i for i, x in enumerate(list_of_money) if x == highest_value]

        return data_list[place_of_value[0]][0]


def sum_sold(file_name):
    with open(file_name) as file:

        data_list = file.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        list_of_money = [data_list[i][int(1)] for i in range(len(data_list))]
        list_of_money = [float(i) for i in list_of_money]
        return sum(list_of_money)


def get_selling_avg(file_name):
    with open(file_name) as file:
        data_list = file.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        list_of_money = [data_list[i][int(1)] for i in range(len(data_list))]
        list_of_money = [float(i) for i in list_of_money]
        return sum(list_of_money)/len(list_of_money)


def count_longest_title(file_name):
    with open(file_name) as file:

        data_list = file.read().splitlines()
        data_list = [item.split('\t') for item in data_list]

        names = [data_list[i][0] for i in range(len(data_list))]

        list_length = len(names)
        name_characters = [len(names[i]) for i in range(list_length)]
        name_characters = [int(i) for i in name_characters]

        return max(name_characters)


def get_date_avg(file_name):
    with open(file_name) as file:
        data_list = file.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        years = [data_list[i][int(2)] for i in range(len(data_list))]
        years = [int(i) for i in years]
        return -(-sum(years)//len(years))


def get_game(file_name, title):
    with open(file_name) as file:

        data_list = file.read().splitlines()
        data_list = [item.split('\t') for item in data_list]

        for i in range(len(data_list)):
            if data_list[i][0] == title:
                wanted_game = data_list[i]

        wanted_game[1] = float(wanted_game[1])
        wanted_game[2] = int(wanted_game[2])

        return wanted_game
