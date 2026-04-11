# Media Folder Icons
Script to set media folder covers on macOS because I was tired of boring old folder icons for my movie folders. For each immediate subdirectory, applies `poster.jpg` as the directory icon.

<img width="555" alt="image" src="https://user-images.githubusercontent.com/6655696/224489967-b76c939c-bb1c-44db-9b66-20d3886dbd61.png">

Looks great in cover flow!

<img width="1026" alt="Screenshot 2023-03-11 at 15 23 13" src="https://user-images.githubusercontent.com/6655696/224489943-ce62b697-7c58-4c4b-919a-f2ea3b68fb12.png">


## Getting Started

### Prerequisites

- macOS
- Python 3

```
# ImageMagick
brew install imagemagick

# pyobjc (recommended in a local virtual environment)
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pyobjc
```

Notes:

- The script prefers `.venv/bin/python` when available.
- If `magick` is available (ImageMagick v7), it will be used automatically.
- Otherwise it falls back to legacy `identify`/`convert` commands.


### Usage
```
./setCovers [-f] <path to media folder>
```
\-f flag overwrites any previously set icon
