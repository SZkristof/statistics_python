def count_games(file_name):

    with open(file_name) as file:
        for i, line in enumerate(file):
            pass
    return (i + 1)


def decide(file_name, year):

    with open(file_name) as file:
        for line in file:
            if str(year) in line:
                return True
        return False


def get_latest(file_name):

    with open(file_name) as file:
        data_list = file.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        list_of_years = []

        for i in range(len(data_list)):
            list_of_years.append(data_list[i][int(2)])

        list_of_years = [int(i) for i in list_of_years]
        indicator_year = int(max(list_of_years))
        indicator_place = list_of_years.index(indicator_year)

        return data_list[indicator_place][0]


def count_by_genre(file_name, genre):

    with open(file_name) as file:
        data_list = file.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        list_of_genres = []

        for i in range(len(data_list)):
            list_of_genres.append(data_list[i][3])
        final_number = list_of_genres.count(genre)
        return final_number


def get_line_number_by_title(file_name, title):
    with open(file_name) as file:
        data_list = file.readlines()
        # data_list.sort()  # without this line the test runs smooth.
        for i, line in enumerate(data_list):
            if str(title) in line:
                return (i+1)
        return ValueError


def get_genres(file_name):
    with open(file_name) as file:
        data_list = file.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        list_of_genres = []
        for i in range(len(data_list)):
            list_of_genres.append(data_list[i][3])
        short_list = sorted(set(list_of_genres), key=str.lower)
        return short_list


def when_was_top_sold_fps(file_name):
    with open(file_name) as file:
        data_list = file.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        list_of_money = []

        for i in range(len(data_list)):
            list_of_money.append(data_list[i][int(1)])
        list_of_money = [float(i) for i in list_of_money]
        highest_value = float(max(list_of_money))
        return highest_value


'''
        list_of_money = [int(i) for i in list_of_money]
        highest_value = float(max(list_of_money))
        return data_list[highest_value][3]
'''