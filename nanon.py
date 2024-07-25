import requests
import json
from colorama import Fore, Style

def read_init_data(filename):
    with open(filename, 'r') as file:
        return file.read().strip()

def user(init_file):
    url = "https://fishapi.xboost.io/index/tglogin"
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "no-cache",
        "content-type": "application/json;charset=UTF-8",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\", \"Microsoft Edge WebView2\";v=\"126\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "Referer": "https://happy-aquarium.xboost.io/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    initData = read_init_data(init_file)
    payload = {
        "initData": initData
    }
    json_payload = json.dumps(payload)
    response = requests.post(url, headers=headers, data=json_payload)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def send_game_action(action_data, auth):
    url = "https://fishapi.xboost.io/zone/user/gameactions"
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": auth,
        "cache-control": "no-cache",
        "content-type": "application/json;charset=UTF-8",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\", \"Microsoft Edge WebView2\";v=\"126\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "Referer": "https://happy-aquarium.xboost.io/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    json_data = json.dumps(action_data)
    response = requests.post(url, headers=headers, data=json_data)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to send action. Status code: {response.status_code}")
        return None

def auto_compose(fish_id, auth):
    if fish_id <= 1:
        print(Fore.RED + f"❌ Tidak cukup ikan dengan angka lebih dari 1 untuk melakukan auto compose untuk fish ID {fish_id}.")
        return
    
    action_data = {
        "actions": [
            {
                "action": "compose",
                "id": fish_id
            }
        ]
    }
    
    result = send_game_action(action_data, auth)
    
    if result:
        print(Fore.GREEN + f"✅ Auto compose untuk fish ID {fish_id} berhasil dijalankan.")
    else:
        print(Fore.RED + f"❌ Gagal melakukan auto compose untuk fish ID {fish_id}.")

def auto_buy(item_id, auth):
    url = "https://fishapi.xboost.io/zone/user/gameactions"
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": auth,
        "cache-control": "no-cache",
        "content-type": "application/json;charset=UTF-8",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\", \"Microsoft Edge WebView2\";v=\"126\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "Referer": "https://happy-aquarium.xboost.io/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    payload = {
        "actions": [
            {
                "action": "buy",
                "id": item_id
            }
        ]
    }
    try:
        json_payload = json.dumps(payload)
        response = requests.post(url, headers=headers, data=json_payload)
        response.raise_for_status()
        if response.status_code == 200:
            print(Fore.GREEN + f" ✅ Item with ID {item_id} successfully purchased.")
            return response.json()
        else:
            print(Fore.RED + f"❌ Failed to make purchase. Insufficient funds!")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def get_task(auth):
    url = "https://fishapi.xboost.io/zone/task/plist"
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": auth,
        "cache-control": "no-cache",
        "content-type": "application/json;charset=UTF-8",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\", \"Microsoft Edge WebView2\";v=\"126\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "Referer": "https://happy-aquarium.xboost.io/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def clear_task(task_id, auth):
    url = "https://fishapi.xboost.io/zone/task/paction"
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": auth,
        "cache-control": "no-cache",
        "content-type": "application/json;charset=UTF-8",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\", \"Microsoft Edge WebView2\";v=\"126\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "Referer": "https://happy-aquarium.xboost.io/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    body = {
        "task_id": task_id
    }
    json_body = json.dumps(body)
    try:
        response = requests.post(url, headers=headers, data=json_body)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def print_welcome_message():
    print(r"""      
▒█▀▀▀█ █▀▀█ ░█▀█░ ▒█▄░▒█ 
░▀▀▀▄▄ ░░▀▄ █▄▄█▄ ▒█▒█▒█ 
▒█▄▄▄█ █▄▄█ ░░░█░ ▒█░░▀█
          """)
    print(Fore.GREEN + Style.BRIGHT + "NanonFish BOT")
    print(Fore.RED + Style.BRIGHT + "Jangan di edit la bang :)\n\n")

def main():
    print_welcome_message()
    init_file = "init.txt"
    data = user(init_file)
    if data:
        level = data.get('data', {}).get('level', '')
        diamond = data.get('data', {}).get('diamond', '')
        gold = data.get('data', {}).get('gold', '')
        fishLimit = data.get('data', {}).get('fishLimit', '')
        fishes = data.get('data', {}).get('fishes', [])
        auth = data.get('data', {}).get('login_token', '')

        choice_clear = input(Fore.BLACK + f"Apakah Anda ingin membersihkan tasks? (y/n): ").strip().lower()
        if choice_clear == 'y':
            task_data = get_task(auth)
            if task_data:
                tasks = task_data.get('data', {}).get('tasks', [])
                for task_group in tasks:
                    for task in task_group.get('tasks', []):
                        task_id_to_clear = task.get('task_id', '')
                        if task_id_to_clear:
                            clear_response = clear_task(task_id_to_clear, auth)
                            if clear_response:
                                print(Fore.GREEN + f"✅ Status clear task {task_id_to_clear}: Successful")
                        else:
                            print("Task ID tidak valid.")

        print("\nDetail Akun:\n")
        print(Fore.BLACK + f"[📊] Level         : {Fore.CYAN + f'{level}'}")
        print(Fore.BLACK + f"[💎] Diamond       : {Fore.BLUE + f'{diamond}'}")
        print(Fore.BLACK + f"[💰] Gold          : {Fore.YELLOW + f'{gold}'}")
        print(Fore.BLACK + f"[⚠️] Fish Limit     : {Fore.LIGHTYELLOW_EX + f'{fishLimit}'}")
        print(Fore.BLACK + f"[🐠] Fish          : {Fore.LIGHTMAGENTA_EX + f'{fishes}'}")
        print("")

        # Pengecekan ikan dengan jumlah lebih dari 1 sebelum menjalankan auto compose
        if any(fishes.count(fish) > 1 for fish in fishes):
            seen = set()
            for fish_id in fishes:
                if fishes.count(fish_id) > 1 and fish_id not in seen:
                    auto_compose(fish_id, auth)
                    seen.add(fish_id)
            else:
                print(Fore.RED + "❌ Tidak cukup ikan dengan angka lebih dari 1 untuk melakukan auto compose.")
        else:
            print(Fore.RED + "❌ Tidak ada ikan dengan angka lebih dari 1 untuk melakukan auto compose.")

        choice_buy = input(Fore.BLACK + f"Apakah Anda ingin melakukan pembelian ikan? (y/n): ").strip().lower()
        if choice_buy == 'y':
            item_id = int(input(Fore.BLACK + f"Masukkan ID ikan yang ingin dibeli : "))
            auto_buy(item_id, auth)
    else:
        print(Fore.RED + f"❌ Gagal mengambil atau tidak ada data user.")

if __name__ == "__main__":
    main()

