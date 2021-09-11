from libqtile import widget
from settings.theme import colors
from libqtile import qtile


# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

base = lambda fg='text', bg='dark': {
	'foreground': colors[fg],
	'background': colors[bg]
}

separator = lambda: widget.Sep(**base(), linewidth =0, padding=8)

icon = lambda fg='text', bg='dark', fontsize=18, text="?": widget.TextBox(
	**base(fg, bg),
	fontsize=fontsize,
	text=text,
	padding=6,
    font="fontawesome"
)

powerline = lambda fg="light", bg="dark": widget.TextBox(
   **base(fg, bg),
	text="", # Icon: nf-oct-triangle_left
	fontsize=37,
	padding=-2
)

workspaces = lambda: [
	widget.GroupBox(
		**base(fg='light'),
		fontsize=22,
		margin_y=3,
		margin_x=3,
		padding_y=2,
		padding_x=2,
		borderwidth=0,
		active=colors['active'],
		inactive=colors['inactive'],
		rounded=True,
		highlight_method='block',
		urgent_alert_method='block',
		urgent_border=colors['urgent'],
		this_current_screen_border=colors['focus'],
		this_screen_border=colors['grey'],
		other_current_screen_border=colors['dark'],
		other_screen_border=colors['dark'],
		disable_drag=True
	),
#    separator(),
	widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
#    separator(),
]

primary_widgets = [
	separator(),
	*workspaces(),
        separator(),
	widget.Systray(**base(bg='dark', fg='color1'),icons_size=30,padding =4),
  widget.TextBox(
        text='|',
        padding=0,
        **base(bg='dark', fg='color3'),
        fontsize=32,
    ),
    icon(bg="dark",fg='color3', fontsize=16, text=' '),
    widget.Volume(
        **base(bg='dark', fg='color3'),
        font="novamono for powerline",
        fontsize=14,
        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("pavucontrol")},
    ),
    widget.TextBox(
        text='|',
        padding=0,
        **base(bg='dark', fg='color4'),
        fontsize=32,
    ),
	icon(bg="dark",fg='color4', fontsize=18, text='  '), # Icon: nf-mdi-calendar_clock
	widget.Clock(**base(bg='dark',fg='color4'), format='%d %b, %A', fontsize=14),
    widget.TextBox(
        text='|',
        padding=0,
        **base(bg='dark', fg='color2'),
        fontsize=32,
    ),
    icon(bg="dark",fg='color2', fontsize=18, text=' '),
    widget.Clock(**base(bg='dark',fg='color2'), format='%I:%M %p', fontsize=14),
    widget.TextBox(
        text='|',
        padding=0,
        **base(bg='dark', fg='color1'),
        fontsize=32,
    ),
    icon(bg="dark", fg='color1', fontsize=18, text='  '),
    widget.Battery(**base(bg='dark', fg='color1'),
        fontsize=15,
        low_percentage=0.2,
        low_foreground=colors['color2'],
        update_interval=1,
        format='{percent:2.0%}',
    ),
    separator(),
]

secondary_widgets = [
	*workspaces(),
	separator(),
	powerline('color1', 'dark'),
]

widget_defaults = {
	'font': 'Cascadia Code',
	'fontsize': 18,
	'padding': 3,
}
extension_defaults = widget_defaults.copy()
