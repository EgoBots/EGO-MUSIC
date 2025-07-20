from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SHUKLAMUSIC import app
from config import BOT_USERNAME
from SHUKLAMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
⦿ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴀᴀʀᴜᴍɪ ᴍᴜsɪᴄ ʀᴇᴘᴏs 
 
 ➲ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✰
 
 ➲ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ɴᴏ ɪᴅ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✰
 
 ➲ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✰
 
 ► ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/AarumiBots"),
          InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/Swagger_Soul"),
          ],
               [
                InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url="https://t.me/AarumiBots"),

],
[
              InlineKeyboardButton("ᴍᴜsɪᴄ ʙᴏᴛ", url=f"https://github.com/EgoBots/EGO-MUSIC/fork"),
              InlineKeyboardButton("︎v2 ᴍᴜsɪᴄ", url=f"https://github.com/EgoBots/EGO-MUSIC/fork"),
              ],
              [
              InlineKeyboardButton("ᴠ1 ᴍᴜsɪᴄ", url=f"https://github.com/EgoBots/EGO-MUSIC/fork"),
InlineKeyboardButton("cʜᴀᴛʙᴏᴛ", url=f"https://github.com/EgoBots/EGO-MUSIC/fork"),
],
[
InlineKeyboardButton("sᴛʀɪɴɢʙᴏᴛ", url=f"https://github.com/EgoBots/EGO-MUSIC/fork"),
InlineKeyboardButton("ᴍᴀɴᴀɢᴇᴍᴇɴᴛ", url=f"https://github.com/EgoBots/EGO-MUSIC/fork"),
],
[
              InlineKeyboardButton("sᴘᴀᴍ ʙᴏᴛ", url=f"https://github.com/EgoBots/EGO-MUSIC/fork"),
              InlineKeyboardButton("ʙᴀɴ-ᴀʟʟ 10 ʙᴏᴛ", url=f"https://github.com/EgoBots/EGO-MUSIC/fork"),
              ],
              [
              InlineKeyboardButton("sᴛʀɪɴɢ ʜᴀᴄᴋ", url=f"https://github.com/EgoBots/EGO-MUSIC/fork"),
InlineKeyboardButton("ɪᴅ ᴄʜᴀᴛ ʙᴏᴛ", url=f"https://github.com/EgoBots/EGO-MUSIC/fork"),
],
[
InlineKeyboardButton("ᴜsᴇʀʙᴏᴛ", url=f"https://github.com/itzshukla/STRANGER-USERBOT3.0/fork"),
InlineKeyboardButton("ɪᴅ-ᴜsᴇʀʙᴏᴛ", url=f"https://t.me/Swagger_Soul"),
],
[
InlineKeyboardButton("sᴜᴘᴇʀ-ᴍᴜsɪᴄ", url=f"https://github.com/EgoBots/EGO-MUSIC/fork"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/1dv6g2.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/EgoBots/EGO-MUSIC/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://github.com/EgoBots/EGO-MUSIC) | [UPDATES](https://t.me/AarumiBots)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")


