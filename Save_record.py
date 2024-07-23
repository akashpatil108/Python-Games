
class Save_record:
    def save_record(self, game_name, player_name, result):
        record = f" Game: {game_name}, Player: {player_name}, Result: {result}\n"
        with open('game_records.txt', 'a') as file:
            file.write(record)
