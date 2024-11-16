import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import random
import time

voice_packs = os.listdir("VoicePacks")
pygame.mixer.init()

if len(voice_packs) == 0:
    raise FileNotFoundError("There are no voice packs detected")
print(f"{len(voice_packs)} voice packs detected")
print("Choose your voice_pack:")
for i , name in enumerate(voice_packs):
    print(f"[{i}] | {name}")
while True:
    user_choice = input()
    try:
        if user_choice in voice_packs:
            voice_lines = os.listdir("VoicePacks\\" + voice_packs[voice_packs.index(user_choice)])
            user_choice = voice_packs[voice_packs.index(user_choice)]
            break
        elif user_choice.isnumeric():
            voice_lines = os.listdir("VoicePacks\\" + voice_packs[int(user_choice)])
            user_choice = voice_packs[int(user_choice)]
            break
    except IndexError:
        print("Error: voice pack not found")


print(f"{len(voice_lines)} voice lines detected")

delay_time = int(input("Set average time between voice lines (minutes): ")) * 60
delay_distribution = int(input("Set standard deviation in time between voice lines (minutes): ")) * 60

if delay_distribution > delay_time:
    raise ValueError("Standard deviation must be more than time between voice lines.")

while True:
    line = random.choice(voice_lines)
    pygame.mixer.music.load(f"VoicePacks\\{user_choice}\\{line}")
    pygame.mixer.music.play()
    exact_delay_time = random.randint(delay_time - delay_distribution, delay_time + delay_distribution)
    time.sleep(exact_delay_time)
    while pygame.mixer.music.get_busy():
        pass
