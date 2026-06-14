player_stats_list = [
    ("Faker", "10", "2", "8"),
    ("ShowMaker", "15", "0", "10"),
    ("Chovy", "12", "ba", "5"),
    ("Gumayusi", "8", "1", "12")
]


def calculate_kda(kills: int, deaths: int, assists: int) -> float:
    if deaths == 0:
        raise ZeroDivisionError
    return (kills + assists) / deaths


def display_kda_leaderboard(stats_list):
    print("--- BẢNG XẾP HẠNG KDA ---")
    
    for player_info in stats_list:
        name = player_info[0]
        raw_kills = player_info[1]
        raw_deaths = player_info[2]
        raw_assists = player_info[3]
        
        try:
            kills = int(raw_kills)
            deaths = int(raw_deaths)
            assists = int(raw_assists)
            
            kda = calculate_kda(kills, deaths, assists)
            print(f"Tuyển thủ {name} có chỉ số KDA là: {kda}")
            
        except ZeroDivisionError:
            print(f"[{name}]: KDA Hoàn hảo (Perfect Game)!")
            continue
            
        except ValueError:
            print(f"[{name}]: Lỗi dữ liệu không hợp lệ!")
            continue


if __name__ == "__main__":
    display_kda_leaderboard(player_stats_list)