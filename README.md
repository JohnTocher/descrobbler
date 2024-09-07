# descrobbler
Utility for parsing scrobbled content for commenting and possibly sharing

I listen to (and scrobble) a bunch of podcasts and music, this project is designed to help me revisit podcasts I've listed to recently, and make a few notes for re-sharing or just further contemplation.

It should separate podcast from music content, and put the two in a place I can easily do something with them later.

Refer to mylast.py for notes regarding some environment variables "LASTFM_API_KEY", "LASTFM_API_SECRET" to be configured for auth

## Usage

```python .\descrobble.py```

## installation

Depends on lastfm_tools:
https://github.com/hugovk/lastfm-tools

and uses dynaconf for configuration management
https://www.dynaconf.com/

```bash
pip install pylast
pip install dynaconf
```

these are in requirements.txt

## configuration


## ToDo

- Import user settings from a text file (including output file location)
- get track duration information
- discriminate between podcasts and music tracks
- store the output in a (mysql?) database
- write up the default settings options

