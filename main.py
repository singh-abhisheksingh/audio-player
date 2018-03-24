import os
import winsound

n = 1
sound_directory = os.listdir("C:/Users/Abhishek/Desktop/audio-player/audio")
print sound_directory
sound_track = []
for song in sound_directory:
	if song.endswith('.wav'):
		sound_track.append(song)

print sound_track
i = 0
winsound.PlaySound(None, winsound.SND_PURGE)

while n:
	n = input("Press 5 to play \nPress 8 to stop \nPress 4 to play previous track \nPress 6 to play next track\n")
	if n == 5:
		winsound.PlaySound(r"C:/Users/Abhishek/Desktop/audio-player/audio/"+sound_track[i], winsound.SND_ASYNC)
	elif n == 8:
		winsound.PlaySound(None, winsound.SND_PURGE)
	elif n == 4:
		i = i-1
		if i == -1:
			i = len(sound_track)-1
		winsound.PlaySound(r"C:/Users/Abhishek/Desktop/audio-player/audio/"+sound_track[i], winsound.SND_ASYNC)
	elif n == 6:
		i = i+1
		if i == len(sound_track):
			i = 0
		winsound.PlaySound(r"C:/Users/Abhishek/Desktop/audio-player/audio/"+sound_track[i], winsound.SND_ASYNC)
	else:
		break