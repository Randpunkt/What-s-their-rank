import webbrowser

print("What's their tag (if their tg is ex. rand#608 write it in the form 'rand-608'):")
player_tag = str(input())
webbrowser.open(str('https://slippi.gg/user/'+player_tag))
