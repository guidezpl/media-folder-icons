# Set Folder Cover
Script to set media folder covers. I was tired of boring old folder icons for my movie folders, so I wrote this bash (+ tiny bit of python) script.

For each immediate subdirectory, applies "folder.jpg" as the subdirectory icon.

![in-progress](https://raw.githubusercontent.com/guidezpl/Set-Folder-Cover/master/in-progress.png)

Looks great in cover flow

![cover-flow](https://raw.githubusercontent.com/guidezpl/Set-Folder-Cover/master/cover-flow.png)

## Getting Started

Tested on Mac OSX High Sierra, but should work on any Unix system.

### Prerequisites

Directory structure:
- Media_Folder/*/folder.jpg

Commands needed: 
- convert, identify (available with ```brew install imagemagick```)
- realpath, basename, dirname
- python


### Usage
```
./setCovers [-f] <path to media folder>
```
\-f flag overwrites any previously set icon

```
eg: ~/User/Downloads/setCovers ~/Movies
```
