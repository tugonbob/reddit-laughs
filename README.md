# Automated Reddit Video Compliation Creation
## Quick Start
```
git clone https://github.com/tugonbob/RedditLaughs.git
pip install -r requirements.txt
# Install FFmpeg (instructions below)
# Edit 'SelectedSubreddits.csv' to your preferred subreddits
python main.py
```


## Installing FFmpeg
### Windows:
https://m.wikihow.com/Install-FFmpeg-on-Windows

(You may need to restart your pc after applying these steps)

### Linux:
```sudo apt install ffmpeg```

### Mac OS:
install Homebrew:
```/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"```
Then:
```brew install ffmpeg```


## Editing SelectedSubreddits.csv

### Subreddit Column
1. Add your desired subreddits with out the 'r/'. 
2. Double check your spelling and casing. 
> The script will just skip over misspelled subreddits
> 
### TimeFilter Column
Get top reddit posts within this time frame.
Options:
- ```hour```
- ```day```
- ```week```
- ```month```
- ```year```
- ```all```

### DesiredDuration Column
The time threshold (in seconds) the videos must reach before moving onto the next subreddit

## Command Line Options
```-v``` or ```-verbose```: to print logs during the scripts execution
