

#Program to swap wallpaper of MacOSX manytime during the day


import subprocess, time, os

#Where is "/Users/macbook/Wallpapers/46670_nissan-skyli$..." is the place to put the image address
SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "/Users/macbook/Wallpapers/iIDPht.jpg"
end tell
END"""

def swap_wallpaper(filepath='macbook/Wallpapers/'):
#path from the /Users/...
#the pattern is my path

    

    print('changing wallpaper...')

    script = f"""/usr/bin/osascript<<END
        tell application "Finder"
        set desktop picture to POSIX file "/Users/{filepath}"
        end tell
        END"""

    try:
        subprocess.Popen(script, shell=True)

        print('wallpaper changed!')
    
    except:
        print('ERROR! something was wrong!')


def organize_files(wallpapers_path='/Users/macbook/Wallpapers/'):
    #the pattern path is '/Users/macbook/Wallpapers/' it's my path
    for count, filename in enumerate(os.listdir(wallpapers_path)):
        new_name = f'wallpaper{count}.png'
        old_name = wallpapers_path+filename
        new_name = wallpapers_path+new_name

        os.rename(old_name, new_name)



organize_files()

c = 0
while True:
    os.system('clear')
    print('Wallpaper selected…')
    time.sleep(1800)
    file_name = f'macbook/Wallpapers/wallpaper{c}.png'
    swap_wallpaper(file_name)
    c += 1



