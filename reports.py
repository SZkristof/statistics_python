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



