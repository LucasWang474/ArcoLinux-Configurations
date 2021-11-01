# Front-end

## grab color

```bash
sudo pacman -S xcolor
```

i3 config:

```bash
##############################################################################
### This i3 binding mode can grab hexadecimal color code of any pixel on the screen,
### and you can move the cursor pixel by pixel via WASD or Arrow keys.
### After grabbing, color code will be automatically copied to clipboard.

### Usage:
### 1. Press mod+g
### 2. Press g
### 3. (Move with WASD or arrow keys) and select any pixel.
### 4. Ctrl+V

# bindsym $mod+g --release exec xcolor -s -S 15 -P 320

bindsym $mod+g mode "$grabc"
set $grabc First press g, then use wasd or arrow keys to move.
mode "$grabc" {
    # bindsym g --release exec xcolor -s -S 15 -P 320
    bindsym g --release exec xcolor -s -S 12 -P 320

    bindsym Left exec xdotool mousemove_relative -- -1 0
    bindsym Right exec xdotool mousemove_relative 1 0
    bindsym Up exec xdotool mousemove_relative -- 0 -1
    bindsym Down exec xdotool mousemove_relative 0 1

    bindsym a exec xdotool mousemove_relative -- -1 0
    bindsym d exec xdotool mousemove_relative 1 0
    bindsym w exec xdotool mousemove_relative -- 0 -1
    bindsym s exec xdotool mousemove_relative 0 1
    
    bindsym Return mode "default"
    bindsym Escape mode "default"
}
##############################################################################
```







# Shell

## [tldr](https://tldr.sh/)

```bash
sudo pacman -S tldr
```



## Alarm clock

```bash
sleep 10s && mpv ~/Music/FILE
sleep 15m && mpv ~/Music/FILE
sleep 1h && mpv ~/Music/FILE
```



## Count video duration

```bash
sudo pacman -S mediainfo

# you may add '-maxdepth NUMBER' option to find
find . -type f -exec mediainfo --Inform="General;%Duration%" "{}" \; 2>/dev/null | awk '{s+=$1/1000} END {h=s/3600; s=s%3600; printf "%.2d:%.2d\n", int(h), int(s/60)}'
```



## Reset password lock

```bash
faillock --user lucas --reset
```



