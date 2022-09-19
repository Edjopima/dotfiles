#!/bin/sh

#!/bin/sh
#nm-applet &
#udiskie -t &
#volumeicon &
#nitrogen --restore &
#cbatticon -u 5 &
xrandr --output eDP-1 --mode 1920x1080 --pos 1920x0 --rotate normal --output HDMI-1-0 --primary --mode 1920x1080 --pos 0x0 --rotate normal &
nm-applet &
udiskie -t &
nitrogen --restore &
cbatticon -u 5 &
volumeicon &
picom &