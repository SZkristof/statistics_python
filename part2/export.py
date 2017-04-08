
# Export functions

import reports


def export():
    with open("export.txt", "w") as file:
        file.write(str(reports.get_most_played("game_stat.txt")) + "\n" +
                   str(reports.sum_sold("game_stat.txt") + "\n" +
                   str(reports.get_selling_avg("game_stat.txt")) + "\n" +
                   str(reports.count_longest_title("game_stat.txt")) + "\n" +
                   str(reports.get_date_avg("game_stat.txt")) + "\n" +
                   str(reports.get_genres("game_stat.txt")) + "\n" +
                   str(reports.get_game("game_stat.txt", "Minecraft")) + "\n")


export()

