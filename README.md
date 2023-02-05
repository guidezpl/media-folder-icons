# Set Folder Cover
Script to set media folder covers on macOS because I was tired of boring old folder icons for my movie folders. For each immediate subdirectory, applies "poster.jpg" as the directory icon.

![in-progress](https://raw.githubusercontent.com/guidezpl/Set-Folder-Cover/master/in-progress.png)

Looks great in cover flow!

![cover-flow](https://raw.githubusercontent.com/guidezpl/Set-Folder-Cover/master/cover-flow.png)

## Getting Started

### Prerequisites

- macOS
- Directory structure: \<path to media folder\>/<Movie/TV folder>/poster.jpg

```
# pyobjc
pip3 install pyobjc --user
# ImageMagick
brew install imagemagick
```


### Usage
```
./setCovers [-f] <path to media folder>
```
\-f flag overwrites any previously set icon
