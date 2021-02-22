set number
set mouse=a
set numberwidth=1
set clipboard=unnamed
syntax on
set showcmd
set ruler
set cursorline
set encoding=utf-8
set showmatch
set sw=2
set relativenumber
so ~/.vim/plugins.vim
so ~/.vim/maps.vim
so ~/.vim/plugin-config.vim

colorscheme onedark 
"set background=dark
let g:onedark_terminal_italics = 1
let g:onedark_termcolors=256
let g:gruvbox_contrast_dark ="hard" 
set laststatus=2
set noshowmode
highlight Normal ctermbg=none
highlight NonText ctermbg=none

" Javascript
"autocmd bufnewfile,bufread *.tsx set filetype=typescript.tsx
"autocmd bufnewfile,bufread *.ts set filetype=typescript.tsx
"autocmd bufnewfile,bufread *.jsx set filetype=javascript.jsx
"autocmd bufnewfile,bufread *.js set filetype=javascript.jsx

"" Searching
set hlsearch                    " highlight matches
set incsearch                   " incremental searching
set ignorecase                  " searches are case insensitive...
set smartcase                   " ... unless they contain at least one capital letter

