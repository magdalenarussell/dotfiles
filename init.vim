set runtimepath^=~/.vim
set runtimepath+=~/.vim/after
let &packpath = &runtimepath
source ~/.vim/vimrc
let g:UltiSnipsSnippetsDir = "~/.vim/UltiSnips"
let g:UltiSnipsSnippetDirectories=["~/.vim/UltiSnips"]
let g:python3_host_prog = '~/.dotfiles/vim/python-vim-env/bin/python'
