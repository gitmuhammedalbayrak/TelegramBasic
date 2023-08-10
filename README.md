## Description

This is a simple Telegram bot that provides an example of using Inline Keyboard to give the user option selection from a main menu. The user sees the main menu on /start command and can interact with the bot by selecting an option from the Inline Keyboard. Different callback handlers are defined for each option. This is a common pattern in Telegram bots.

# Telegram Inline Keyboard Bot

This repo contains an example of building a simple menu bot using Inline Keyboard in Telegram.

## Requirements

- Python 3.6+ 
- python-telegram-bot==13.13

## Setup

1. Clone the repo

```bash
git clone https://github.com/yourusername/telegram-inline-keyboard-bot.git
```

2. Install requirements

```bash
pip install -r requirements.txt
```

3. Replace `TOKEN` constant with your bot token from Telegram.

4. Run `main.py`

```bash
python main.py
```

The bot should now be up and running. You can start chatting with it on Telegram via @botusername.

## Usage

Display main menu with `/start` command. Then select an option from the Inline Keyboard. Each option has a different handler. 

## Contributing

Pull requests are welcome. Please keep code quality high.

## License

[MIT](https://choosealicense.com/licenses/mit/)
