# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Qtile workspaces

from libqtile.config import Key, Group, Match
from libqtile.command import lazy
from settings.keys import mod, keys

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
# Icons: 
# nf-fa-firefox, 
# nf-dev-terminal, 
# nf-fa-code, 
# nf-seti-config, 
# nf-mdi-folder, 
# nf-mdi-image, 
# nf-fa-video_camera, 


#groups = [Group(i) for i in [
#    "   ", "   ", "   ","   ", "   ",
#]]

groups = [
    Group("   ", matches=[Match(title='Mozilla Firefox'),Match(title='Google Chrome')]),
    Group("   ", matches=[Match(title='Visual Studio Code')]),
    Group("   ", matches=[Match(title='Discord'), Match(title='Slack'), Match(title='Telegram')]),
    Group("   ", matches=[Match(title='Spotify Free')]),
    Group("   ", matches=[Match(title='pcmanfm')]),
]

for i, group in enumerate(groups):
     actual_key = str(i + 1)
     keys.extend([
         # Switch to workspace N
         Key([mod], actual_key, lazy.group[group.name].toscreen()),
         # Send window to workspace N
         Key([mod, "shift"], actual_key, lazy.window.togroup(group.name)),
     ])
