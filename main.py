import pytchat
import requests
import urllib.parse

video_id = "paqznnyTJ0k"

def main():
    chat = pytchat.create(video_id)
    try:
        while chat.is_alive():
            for c in chat.get().sync_items():
                print(f"{c.datetime} [{c.author.name}]- {c.message}")
                urlmessage1 = c.message
                send = []
                send.append(urlmessage1)
                send.append(c.author.name)
                send = urllib.parse.quote(str(send))
                requests.get(f"https://snapextensions.uni-goettingen.de/handleTextfile.php?type=write&content={send}&filename=./textfiles/logiselive.yt")
                
                if(c.type == "superChat"):
                    print("Thanks for the Super chat")
    except Exception as e:
        # TODO: Parse error logs
        print(e)
        print(f"Exception occured with the payload: {c.message}")
        exit()

print("********Started YouTube Server********")
print("======================================")
main()
