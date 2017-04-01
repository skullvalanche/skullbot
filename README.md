# Skullbot
A Python based IRC/TwitchBot

# Instructions
1. Clone the repo
1. Save a copy of `example_responses.json` as `responses.json` -- modify it with whatever responses you wish.
1. Log in to http://twitch.tv/ as your bot. (Your bot will need a twitch account)
1. Go to https://twitchapps.com/tmi/ and authenticate as your bot to get an OAuth token.
1. Save a copy of `example_settings.py` as `settings.py`.
1. Edit `settings.py` with your bot's information.
1. Run `python skullbot.py`
1. Profit

## Responses
- Skullbot's responses are stored in a JSON file.
- Skullbot's responses have 'triggers' which are keywords or phrases.
- Skullbot's triggers also support Regular Expressions (RegEx).
- Skullbot's responses can be a single phrase, or a randomly chosen phrase from a list.
- Skullbot's triggers can also have aliases, thus you can have many triggers which point to one response, or many triggers which point to a list of possible responses.

Please look at `example_responses.json` for how to properly format.

