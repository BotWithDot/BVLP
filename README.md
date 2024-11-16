# BVLP - Background Voice Line Player

BVLP is a player that plays voice lines periodically. You can choose the delay between voice lines and add a variation to that delay.

## How to use
**<ins>Before starting</ins>**, you need to add a folder with audio files to the "VoicePacks" folder. You can use WAV, MP3, or OGG audio files.  
Once you start the code, you will get an option to select one of the voice packs you added. You can select the pack by entering an index or the name of the folder.  
After you select the pack, you need to choose the delay between the voice lines in minutes. The delay cannot be less than 0.  
After that, you can choose a delay time distribution in minutes. The distribution cannot be less than 0, and the total delay cannot be higher than the delay time.  
> [!NOTE]  
> The minimum delay time will be calculated by decreasing the distribution time from the delay time, and the maximum delay time will be calculated by adding the distribution time to the delay time.  
> ```
> exact_delay_time = random.randint(delay_time - delay_distribution, delay_time + delay_distribution)
> ```  
After setting the delay and distribution, the player will play a random voice line from the selected pack periodically.  

Enjoy!
