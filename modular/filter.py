################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || Gojo_Satoru
"""
################################################################

from re import escape as re_escape
from secrets import choice

from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.types import *

from Mix import *
from Mix.core.sender_tools import send_cmd

__modles__ = "Filter"
__help__ = get_cgr("help_filr")

# Initialise
db = Filters()


@ky.ubot("filters", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    filters_chat = f"{em.sukses} Daftar filters digrup <b>{m.chat.title}</b>:\n"
    all_filters = db.get_all_filters(m.chat.id)
    actual_filters = [j for i in all_filters for j in i.split("|")]
    if not actual_filters:
        await m.reply_text(f"{em.gagal} Tidak ada filters digrup ini.")
        return

    filters_chat += "\n".join(
        [
            f" • {' | '.join([f'<code>{i}</code>' for i in i.split('|')])}"
            for i in all_filters
        ],
    )
    return await m.reply_text(filters_chat, disable_web_page_preview=True)


@ky.ubot("filter", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    args = m.text.split(" ", 1)
    all_filters = db.get_all_filters(m.chat.id)
    actual_filters = {j for i in all_filters for j in i.split("|")}

    if (len(all_filters) >= 50) and (len(actual_filters) >= 150):
        await m.reply_text(
            f"{em.gagal} Anda mempunyai 50 kata filter, hapus salah satu dan coba lagi.",
        )
        return

    if not m.reply_to_message and len(m.text.split()) < 3:
        return await m.reply_text(
            f"{em.gagal} Format yang anda berikan salah. Gunakan format : `filter [nama filter] [balas ke pesan]`."
        )

    if m.reply_to_message and len(args) < 2:
        return await m.reply_text(
            f"{em.gagal} Format yang anda berikan salah. Gunakan format : `filter [nama filter] [balas ke pesan]`."
        )

    extracted = await split_quotes(args[1])
    keyword = extracted[0].lower()

    for k in keyword.split("|"):
        if k in actual_filters:
            return await m.reply_text(f"{em.sukses} Filter <code>{k}</code> sudah ada!")

    if not keyword:
        return await m.reply_text(
            f"{em.gagal} <code>{m.text}</code>\n\nSilahkan berikan nama filter.",
        )

    if keyword.startswith("<") or keyword.startswith(">"):
        return await m.reply_text(
            f"{em.gagal} Tidak dapat menyimpan filter dengan symbol '<' atau '>'."
        )

    eee, msgtype, file_id = get_filter_type(m)
    lol = eee if m.reply_to_message else extracted[1]
    teks = lol if msgtype == Types.TEXT else eee

    if not m.reply_to_message and msgtype == Types.TEXT and len(m.text.split()) < 3:
        return await m.reply_text(
            f"{em.gagal} <code>{m.text}</code>\n\nError: Tidak ada pesan disini!",
        )

    if not teks and not msgtype:
        return await m.reply_text(
            f"{em.gagal} Pastikan split quote sudah benar untuk format filter!",
        )

    if not msgtype:
        return await m.reply_text(
            f"{em.gagal} Pastikan format sudah benar untuk filter!",
        )

    add = db.save_filter(m.chat.id, keyword, teks, msgtype, file_id)
    if add:
        await m.reply_text(
            f"{em.sukses} Filter disimpan '<code>{'|'.join(keyword.split('|'))}</code>'.",
        )
    await m.stop_propagation()


@ky.ubot("unfilter", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    args = c.get_arg(m)

    if len(args) < 1:
        return await m.reply_text(f"{em.gagal} Filter apa yang harus dihentikan ?")

    chat_filters = db.get_all_filters(m.chat.id)
    act_filters = {j for i in chat_filters for j in i.split("|")}

    if not chat_filters:
        return await m.reply_text(f"{em.gagal} Tidak ada filter disini.")

    for keyword in act_filters:
        if keyword == m.text.split(None, 1)[1].lower():
            db.rm_filter(m.chat.id, m.text.split(None, 1)[1].lower())
            await m.reply_text(
                f"{em.sukses} Filter berhasil dihapus!",
            )
            await m.stop_propagation()
        else:
            db.rm_filter(m.chat.id, args)
            await m.reply_text(
                f"{em.sukses} Filter berhasil dihapus!",
            )
            await m.stop_propagation()

    await m.reply_text(
        f"{em.gagal} Tidak ada filters disini!",
    )
    await m.stop_propagation()


@ky.ubot("unfilterall", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    all_bls = db.get_all_filters(m.chat.id)
    if not all_bls:
        return await m.reply_text(f"{em.gagal} Tidak ada filter digrup ini!")
    db.rm_all_filters(m.chat.id)
    await m.reply_text(f"{em.sukses} Semua filter berhasil dihapus!")


async def send_filter_reply(c: user, m, trigger: str):
    em = Emojik()
    em.initialize()
    """Reply with assigned filter for the trigger"""
    getfilter = db.get_filter(m.chat.id, trigger)
    if m and not m.from_user:
        return

    if not getfilter:
        return await m.reply_text(
            "<b>Error:</b> Tidak dapat menemukan filter ini!!",
        )

    msgtype = getfilter["msgtype"]
    if not msgtype:
        return await m.reply_text("<b>Error:</b> Tidak dapat menemukan filter ini!!")
    yoki = await send_cmd(c, msgtype)
    try:
        # support for random filter texts
        splitter = "%%%"
        filter_reply = getfilter["filter_reply"].split(splitter)
        filter_reply = choice(filter_reply)
    except KeyError:
        filter_reply = ""

    parse_words = [
        "first",
        "last",
        "fullname",
        "id",
        "mention",
        "username",
        "chatname",
    ]
    text = await escape_mentions_using_curly_brackets(m, filter_reply, parse_words)
    textt = text
    try:
        if msgtype == Types.TEXT:
            await m.reply_text(
                textt,
                disable_web_page_preview=True,
            )
            return

        elif msgtype in (
            Types.STICKER,
            Types.VIDEO_NOTE,
            Types.CONTACT,
            Types.ANIMATED_STICKER,
        ):
            await yoki(
                m.chat.id,
                getfilter["fileid"],
                reply_to_message_id=m.id,
            )
        else:
            await yoki(
                m.chat.id,
                getfilter["fileid"],
                caption=textt,
                reply_to_message_id=m.id,
            )
    except Exception as ef:
        await m.reply_text(f"Error in filters: {ef}")
        return msgtype

    return msgtype


@user.on_message(filters.text & ~filters.me & ~filters.bot, group=99)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    chat_filters = db.get_all_filters(m.chat.id)
    actual_filters = {j for i in chat_filters for j in i.split("|")}

    for trigger in actual_filters:
        pattern = r"( |^|[^\w])" + re_escape(trigger) + r"(|$|[^\w])"
        match = await regex_searcher(pattern, m.text.lower())
        if match:
            try:
                await send_filter_reply(c, m, trigger)
            except Exception as ef:
                await m.reply_text(f"Error: {ef}")
                LOGGER.error(ef)
                LOGGER.error(format_exc())
            break
        continue
    return
