import requests
import sys
import subprocess

query = input("Enter Your Search : ")
res = requests.get("https://torrent-api-1337x.herokuapp.com/"+query).json()
print(f"Searching for {query}.....\n")

magnet_list = []

for index in range(len(res)):
    print(f"{index+1}  : {res[index]['Name']}\tSize : {res[index]['size']}\n\tSeeder : {res[index]['seeders']}\n")
    magnet_list.append(res[index]['magnet'])


user_choice = int(input("Enter Index : "))

if user_choice > len(res):
    print("\nInValid index")
    print("Exiting.....")

else:
    magnet_link = magnet_list[user_choice -1]
    stream_choice = int(input("Enter 1 to stream or 2 to download Torrent : "))

    window_cmd = f"""webtorrent "{magnet_link}" """
    linux_cmd= f"""webtorrent "{magnet_link}" """

    if stream_choice == 1:

        if sys.platform.startswith('linux'):
            subprocess.call(linux_cmd+"--vlc")

        elif sys.platform.startswith('win32'):
            subprocess.call(window_cmd+"--vlc",shell=True)
    elif stream_choice == 2:

        if sys.platform.startswith('linux'):
            subprocess.call(linux_cmd)

        elif sys.platform.startswith('win32'):
            subprocess.call(window_cmd,shell=True)
    else:
        print("\nInvalid Choice ")
        print("\nExiting....")

        


