# AutoSendDiscordMessage
AutoSendDiscordMessage is a simple Python script designed to automate the sending of messages through your Discord account at regular intervals without the need for manual intervention.

## Features
- Ease of Use: Set it up easily by filling out the configuration in the config.json file.
- Automation: The script continuously sends messages based on the specified time interval.

## Setup
1. **Fill Out The Config**:
- Open the config.json file and provide the necessary information.
2. **Run the Script:**
- Execute the command python main.py in your terminal.
3. **Done!**
- Your script is now running, sending messages automatically based on the specified configuration.
4. **Customization:**
- If you wish to make further changes, feel free to explore and modify the script according to your preferences.

## How To Get Discord Token

1. **Access Discord Web:**
- Open Discord in your web browser.
2. **Open Console:**
-  Right-click anywhere on the page and select 'Inspect' or press Ctrl + Shift + I to open the Developer Tools. Go to the 'Console' tab.
3. **Run Command:**
- Paste the following command in the console:
```js
webpackChunkdiscord_app.push([[""],{},req=>copy(Object.values(req.c).find(x => x?.exports?.default?.getToken).exports.default.getToken())])
```
4. **Token Retrieval:**
- Your Discord token should now be copied to your clipboard, ready to be pasted into the config.json file.
