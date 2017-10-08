<h1 align="center">YAFO</h1>
<p align="center">Yet Another File Organizer: Organize those messy downloads or desktop folders of yours in a jiffy.</p>

<p align="center">
<a href="https://asciinema.org/a/nCFfuGjTNggu2JS4HxX9Nvn8z"><img src="https://imgur.com/DlkebLm.gif" alt="Asciicast" width="734"/></a>
</p>
# 


## Installation
```bash
> git clone https://github.com/prakashdanish/yafo
> cd yafo
> sudo ./install.sh
> cd required_directory
> yafo.py
```

## Usage
User defined rules:
```bash
> yafo.py [-e] [extension(s)] [-d] [directory_name]

options:
-e, --extensions        extension(s) separated by space
-d, --directory         directory name
```
## Note
Don't run `test/cleanup.sh`. It's for testing and may cause damage.

