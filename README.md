# Python-PDF-read-write-sample

# Setup

You have to install brew and pyenv

```
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ brew install pyenv
```

You have to check bash or zsh then setup.

```
$ echo $SHELL

-> /bin/bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
source ~/.bash_profile

-> /bin/zsh
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
source ~/.zshrc
```

You have to install Python PDF library

```
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$ python3 get-pip.py
$ pip3 install pypdf2
$ pip3 install reportlab
```

# Sample

1. Create PDF

```
$ python3 pdf_sample.py
```

2. Create PDF and Write text

```
$ python3 pdf_sample_text.py
```

3. Create PDF and Write text and Merge PDF

```
$ python3 pdf_sample_write.py
```

4. Create PDF and Write text and Merge PDF for 'shibuya_sample.pdf'

```
$ python3 pdf_shibuya_sample.py
```


