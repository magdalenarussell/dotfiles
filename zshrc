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
export PATH="/Users/magdalenarussell/.pixi/bin:$PATH"


export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
export PATH="$HOME/.local/bin:$PATH"
export PATH="$HOME/.local/bin:$PATH"

# bun completions
[ -s "/Users/magdalenarussell/.bun/_bun" ] && source "/Users/magdalenarussell/.bun/_bun"

# bun
export BUN_INSTALL="$HOME/.bun"
export PATH="$BUN_INSTALL/bin:$PATH"
