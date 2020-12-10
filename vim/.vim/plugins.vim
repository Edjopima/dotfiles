call plug#begin('~/.vim/plugged')

"Themes
Plug 'morhetz/gruvbox'
Plug 'flazz/vim-colorschemes'
Plug 'mhartington/oceanic-next'
Plug 'dracula/vim', { 'as': 'dracula' }
Plug 'shinchu/lightline-gruvbox.vim'

"IDE
	"MOVIMIENTO DENTRO Y ENTRE ARCHIVOS
Plug 'easymotion/vim-easymotion'
Plug 'scrooloose/nerdtree'  
Plug 'christoomey/vim-tmux-navigator'
	"BUSCADOR
Plug 'junegunn/fzf', {'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
	"JAVASCRIPT
Plug 'pangloss/vim-javascript' 
Plug 'leafgarland/typescript-vim'
Plug 'mxw/vim-jsx'
Plug 'elzr/vim-json'
Plug 'mattn/emmet-vim'
	"AUTOCOMPLETADO
Plug 'neoclide/coc.nvim',{ 'branch':'release'}
" status bar
Plug 'maximbaz/lightline-ale'
Plug 'itchyny/lightline.vim'
	"WakaTime
Plug 'wakatime/vim-wakatime'
	"Color Picker
Plug 'DougBeney/pickachu'

Plug 'sheerun/vim-polyglot'
" typing
Plug 'jiangmiao/auto-pairs'
Plug 'alvan/vim-closetag'
Plug 'tpope/vim-surround'

" git
Plug 'tpope/vim-fugitive' 

call plug#end()

