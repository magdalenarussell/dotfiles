#!/bin/bash
set -eu

prefix=~/.dotfiles/vim

[ -d $prefix/python-vim-env ] || python3 -m venv $prefix/python-vim-env
source $prefix/python-vim-env/bin/activate
pip install -r $prefix/nvim-requirements.txt

pythonpath=$(which python)
echo Ensure the following are set in init.vim:
echo
echo "let g:python3_host_prog = '${pythonpath}'"
echo
echo "to see path to init.vim run \`:echo stdpath('config')\` in nvim session"
echo "detailed instructions at https://github.com/deoplete-plugins/deoplete-jedi/wiki/Setting-up-Python-for-Neovim#using-virtual-environments"

deactivate
