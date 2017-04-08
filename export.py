import reports


def export():
    with open("export.txt", "w") as file:
        file.write(str(reports.count_games("game_stat.txt")) + "\n" +
                   str(reports.decide("game_stat.txt", 2000)) + "\n" +
                   str(reports.get_latest("game_stat.txt")) + "\n" +
                   str(reports.count_by_genre("game_stat.txt", "RPG")) + "\n" +
                   str(reports.get_line_number_by_title("game_stat.txt", "Minecraft")) + "\n" +
                   str(reports.get_genres("game_stat.txt")) + "\n" +
                   str(reports.when_was_top_sold_fps("game_stat.txt")) + "\n")

export()

