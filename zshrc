clear
umask 007
# stop start output
stty -ixon
autoload -Uz compinit
compinit
export EDITOR="nvim"


## antigen stuff
source $HOME/.antigen/antigen.zsh
# Load the oh-my-zsh's library.
antigen use oh-my-zsh
#antigen bundle virtualenv
#antigen bundle virtualenvwrapper
antigen bundle zsh-users/zsh-syntax-highlighting
antigen bundle zsh-users/zsh-history-substring-search
antigen theme https://gist.github.com/willdumm/c672692545433a858303c079b64955ca gallifrey-nve
# Tell antigen that you're done.
antigen apply

fpath=(~/.zsh $fpath)
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
[ -f ~/.zshrc_machine_specific ] && source ~/.zshrc_machine_specific

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/Users/magdalenarussell/miniconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/Users/magdalenarussell/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/Users/magdalenarussell/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/Users/magdalenarussell/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

