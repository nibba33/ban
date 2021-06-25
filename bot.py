    import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = ':)

    async def kick(message,*args):
        """Kicks the specified user from the server"""
        if len(message.mentions) < 1:
            return False

        if message.channel.is_private:
            msg = await client.send_message(message.channel,'Users cannot be kicked/banned from private channels.')
            asyncio.ensure_future(message_timeout(msg, 40))
            return

        if not message.channel.permissions_for(message.server.get_member(client.user.id)).kick_members:
            msg = await client.send_message(message.channel, message.author.mention + ', I do not have permission to kick users.')
            asyncio.ensure_future(message_timeout(msg, 40))
            return

        members = []

        if not message.channel.is_private and message.channel.permissions_for(message.author).kick_members:
            for member in message.mentions:
                if member != message.author:
                    try:
                        await client.kick(member)
                        members.append(member.name)
                    except:
                        pass
                else:
                    msg = await client.send_message(message.channel, message.author.mention + ', You should not kick yourself from a channel, use the leave button instead.')
                    asyncio.ensure_future(message_timeout(msg, 40))
        else:
            msg = await client.send_message(message.channel, message.author.mention + ', I do not have permission to kick users, or this is a private message channel.')
            asyncio.ensure_future(message_timeout(msg, 40))

        msg = await client.send_message(message.channel,'Successfully kicked user(s): `{}`'.format('`, `'.join(members)))
        asyncio.ensure_future(message_timeout(msg, 60))

    @register('ban','@<mention users>',owner=True)

    async def ban(message,*args):
        """Bans the specified user from the server"""
        if len(message.mentions) < 1:
            return False

        if message.channel.is_private:
            msg = await client.send_message(message.channel,'Users cannot be kicked/banned from private channels.')
            asyncio.ensure_future(message_timeout(msg, 40))
            return

        if not message.channel.permissions_for(message.server.get_member(client.user.id)).ban_members:
            msg = await client.send_message(message.channel, message.author.mention + ', I do not have permission to ban users.')
            asyncio.ensure_future(message_timeout(msg, 40))
            return

        members = []

        if message.channel.permissions_for(message.author).ban_members:
            for member in message.mentions:
                if member != message.author:
                    try:
                        await client.ban(member)
                        members.append(member.name)
                    except:
                        pass
                else:
                    msg = await client.send_message(message.channel, message.author.mention + ', You should not ban yourself from a channel, use the leave button instead.')
                    asyncio.ensure_future(message_timeout(msg, 40))
        else:
            msg = await client.send_message(message.channel, message.author.mention + ', I do not have permission to ban users, or this is a private message channel.')
            asyncio.ensure_future(message_timeout(msg, 40))

        msg = await client.send_message(message.channel,'Successfully banned user(s): `{}`'.format('`, `'.join(members)))
        asyncio.ensure_future(message_timeout(msg, 30))

    @register('bans',alias='bannedusers')
    @register('bannedusers')


if __name__ == "__main__":
    bot = CsakBan()
    bot.run("ODU4MDczOTI5MDAzNjk2MTI4.YNY1ng.q5iXEXJYyJVrnO7ni871HbIMXws")
