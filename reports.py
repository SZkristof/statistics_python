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
    with open(file_name) as f:
        data_list = f.read().splitlines()
        data_list = [item.split('\t') for item in data_list]
        #lets continue here

