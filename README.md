# Set Folder Cover
Script to set media folder covers because I was tired of boring old folder icons for my movie folders. For each immediate subdirectory, applies "folder.jpg" as the directory icon.

![in-progress](https://raw.githubusercontent.com/guidezpl/Set-Folder-Cover/master/in-progress.png)

Looks great in cover flow!

![cover-flow](https://raw.githubusercontent.com/guidezpl/Set-Folder-Cover/master/cover-flow.png)

## Getting Started

Tested on Mac OSX High Sierra, but should work on any Unix system.

### Prerequisites

Directory structure: \<media folder\>/*/folder.jpg

```brew install imagemagick```


### Usage
```
./setCovers [-f] <path to media folder>
```
\-f flag overwrites any previously set icon
