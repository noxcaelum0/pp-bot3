import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Login As：', client.user)
    game = discord.Game('你媽')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "Hi" or message.content == "嗨":
        await message.channel.send('閉嘴')

    if message.content.startswith('說'):
      tmp = message.content.split(" ",2)
      if len(tmp) == 1:
        await message.channel.send("你要我說什麼啦?")
      else:
        await message.channel.send(tmp[1])

 if message.content == 'pp':
        await message.channel.send('8D')

client.run("MTEyODE4MDk1MjY1NzU3MTg4MA.Gxy8gV.yxeSeh72bCr7tySoy6uNAIETQaLpwjEc2lv_fk")
