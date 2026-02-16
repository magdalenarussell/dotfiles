clear
umask 007
# stop start output
stty -ixon
autoload -Uz compinit
compinit
export EDITOR="nvim"
export PATH="/Library/TeX/texbin:$PATH"

## antigen stuff
source $HOME/.antigen/antigen.zsh
# Load the oh-my-zsh's library.
antigen use oh-my-zsh
#antigen bundle virtualenv
#antigen bundle virtualenvwrapper
antigen bundle zsh-users/zsh-syntax-highlighting
antigen bundle zsh-users/zsh-history-substring-search
antigen theme https://gist.github.com/magdalenarussell/8d780187eaadd5e95e60309dc8806476 gallifrey-nve
# Tell antigen that you're done.
antigen apply

fpath=(~/.zsh $fpath)
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
[ -f ~/.zshrc_machine_specific ] && source ~/.zshrc_machine_specific

export PATH="/net/dewitt/vol1/home/magruss/.pixi/bin:$PATH"
export PATH="$HOME/.dotfiles/bin:$PATH"

# >>> mamba initialize >>>
# !! Contents within this block are managed by 'micromamba shell init' !!
export MAMBA_EXE='/net/dewitt/vol1/home/magruss/y/micromamba';
export MAMBA_ROOT_PREFIX='/net/dewitt/vol1/home/magruss/micromamba';
__mamba_setup="$("$MAMBA_EXE" shell hook --shell zsh --root-prefix "$MAMBA_ROOT_PREFIX" 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__mamba_setup"
else
    alias micromamba="$MAMBA_EXE"  # Fallback on help from micromamba activate
fi
unset __mamba_setup
# <<< mamba initialize <<<

alias conda='micromamba'
