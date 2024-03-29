from pyrogram.enums import *
from pyrogram.errors import ChatAdminRequired, UserNotParticipant
from pyrogram.types import *

from Mix import *

__modles__ = "Join"
__help__ = get_cgr("help_join")


@ky.ubot("join", sudo=True)
@ky.devs("Cjoin")
async def _(c, m):
    em = Emojik()
    em.initialize()
    Nan = m.command[1] if len(m.command) > 1 else m.chat.id
    ceger = await m.reply_text(cgr("proses").format(em.proses))
    try:
        chat_id = m.command[1] if len(m.command) > 1 else m.chat.id
        if chat_id.startswith("https://t.me/"):
            chat_id = chat_id.split("/")[-1]
        inpogc = await c.get_chat(Nan)
        namagece = inpogc.title

        await ceger.edit(cgr("join_1").format(em.sukses, namagece))
        await c.join_chat(Nan)
    except Exception as ex:
        await ceger.edit(f"{em.gagal} <b>ERROR: </b>\n\n<code>{str(ex)}</code>")


@ky.ubot("leave|kickme", sudo=True)
@ky.devs("Cleave")
async def _(c, m):
    em = Emojik()
    em.initialize()

    try:
        chat_id = m.chat.id

        if chat_id in NO_GCAST:
            return await m.reply(cgr("join_2").format(em.gagal))

        if str(chat_id).startswith("https://t.me/"):
            chat_id = chat_id.split("/")[-1]
            inpogc = await c.get_chat(chat_id)
            namagece = inpogc.title
            ceger = await m.reply(f"{em.proses} <code>Processing...</code>")
            if str(chat_id) in NO_GCAST or inpogc.id in NO_GCAST:
                await ceger.edit(cgr("join_2").format(em.gagal))
            else:
                await c.leave_chat(chat_id)
                await ceger.edit(
                    cgr("join_4").format(em.sukses, c.me.mention, namagece)
                )
        else:
            await m.reply(cgr("join_5").format(em.sukses))
            await c.leave_chat(chat_id)

    except ChatAdminRequired:
        await m.reply(
            f"{em.gagal} <b>Saya tidak memiliki izin untuk meninggalkan obrolan ini!</b>"
        )
    except UserNotParticipant:
        await m.reply(
            f"{em.gagal} <b>Anda bukan anggota atau member di <code>{namagece}</code></b>"
        )
    except Exception as e:
        await m.reply(
            f"{em.gagal} <b>Terjadi kesalahan saat mencoba meninggalkan obrolan:</b> <code>{str(e)}</code>"
        )


@ky.ubot("leaveallgc|kickmeallgc", sudo=True)
async def _(c, m):
    em = Emojik()
    em.initialize()
    xenn = await m.reply_text(
        f"{em.proses} <code>Global Leave from group chats...</code>"
    )
    luci = 0
    nan = 0
    ceger = [-1001986858575, -1001876092598, -1001812143750]

    async for dialog in c.get_dialogs():
        if dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                chat_info = await c.get_chat_member(chat, "me")
                user_status = chat_info.status
                if chat not in ceger and user_status not in (
                    ChatMemberStatus.OWNER,
                    ChatMemberStatus.ADMINISTRATOR,
                ):
                    nan += 1
                    await c.leave_chat(chat)
            except BaseException:
                luci += 1
    await xenn.edit(cgr("join_6").format(em.sukses, nan, em.gagal, luci))


@ky.ubot("leaveallch|kickmeallch", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    xenn = await m.reply(f"{em.proses} <b>Proses Pengeluaran Global Channel...</b>")
    luci = 0
    nan = 0
    ceger = [-1001713457115, -1001818398503, -1001697717236]

    async for dialog in c.get_dialogs():
        try:
            if dialog.chat.type == ChatType.CHANNEL:
                chat = dialog.chat.id
                try:
                    chat_info = await c.get_chat_member(chat, "me")
                    user_status = chat_info.status
                    if chat not in ceger and user_status not in (
                        ChatMemberStatus.OWNER,
                        ChatMemberStatus.ADMINISTRATOR,
                    ):
                        luci += 1
                        await c.leave_chat(chat)
                except Exception:
                    nan += 1
        except Exception:
            nan += 1
    await xenn.edit_text(cgr("join_7").format(em.sukses, luci, em.gagal, nan))
