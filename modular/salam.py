# Part Of Ayiin-Userbot

import asyncio

from pyrogram import *

from Mix import *

__modles__ = "Salam"
__help__ = "Salam"


@ky.ubot("p", sudo=True)
async def _(c: user, m):
    await m.edit("**Assalamualaikum Anak anjingggg**")


@ky.ubot("pe", sudo=True)
async def _(c: user, m):
    await m.edit("**Assalamualaikum Warahmatullahi Wabarakatuh**")


@ky.ubot("l", sudo=True)
async def _(c: user, m):
    await m.edit("**Wa'alaikumsalam kaum dajjal 🤪**")


@ky.ubot("a", sudo=True)
async def _(c: user, m):
    me = await c.get_me()
    xx = await m.edit(f"**Haii Salken Saya {me.first_name}**")
    await asyncio.sleep(1)
    await xx.edit("**Assalamualaikum**")


@ky.ubot("j", sudo=True)
async def _(c: user, m):
    xx = await m.edit("**JAKA SEMBUNG BAWA GOLOK**")
    await asyncio.sleep(1)
    await xx.edit("**NIMBRUNG GOBLOKK!!!🔥**")


@ky.ubot("k", sudo=True)
async def _(c: user, m):
    me = await c.get_me()
    xx = await m.edit(f"**Hallo KIMAAKK SAYA {me.first_name}**")
    await asyncio.sleep(1)
    await xx.edit("**LU SEMUA NGENTOT 🔥**")


@ky.ubot("ass", sudo=True)
async def _(c: user, m):
    xx = await m.edit("**Salam Dulu Biar Sopan**")
    await asyncio.sleep(1)
    await xx.edit("**السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ**")