import discord
# use python3 -m pip install -U discord.py
import seaborn as sb
import random
import zf_front
import pandas as df
from discord.ext import commands

intents = discord.Intents(messages=True,
                          guilds=True,
                          reactions=True,
                          members=True,
                          presences=True)
intents = discord.Intents.all()
client = commands.Bot(command_prefix='zofia ',
                      intents=intents,
                      help_command=None)


@client.command()
async def help(context):
    helptext = " ```ini\n[Sharky Beta V1.0]\nSharky is a chat bot who can reply to simple questions with a few preset answers. To talk to her, just type \"Sharky \" followed by your question or sentence. you can also just have the word \"Sharky\" in your sentence and it will work fine. This process is mostly buggy and she will not answer to specific types of questions but when found out, will be added in future updates\nSharky can also occasionally respond to specific songs and sing along with you should you type the lyrics\nSome sample questions and phrases you can try you can try out:\nSharky what would you like to eat?\nSharky who do you like the most\nSharky will this server be successful?\nSharky what should I drink?\nSharky hello\nSharky bye\nYou are my fire\n[Note: Sharky will mostly be offline. you can ask me whenever you want to try her out and I will bring her online when I can]```"
    await context.send(helptext)



# Question answer stuff
  
def qna(ques):
  #Null do
    if 'do' in ques and not 'want' in ques and not "like" in ques:
        ans = 'Your mom'
    else:
      
# Check for food
      
        if 'food' in ques or 'eat' in ques:
            if 'you' in ques or 'your' in ques:
                obj = ['Icecream', 'borgar']
            else:
                obj = [
                    'food', 'pizza', 'fried rice', 'sandwich', 'borgar',
                    'dog food', 'air', 'McDonalds but at home', 'tide pods',
                    'bar of soap', 'sushi', 'ramen', 'pasta'
                ]
              
# Check for drink
              
        elif 'drink' in ques:
            if 'you' in ques or 'your' in ques:
                obj = ['Strawberry milkshake', 'apple juice']
            else:
                obj = [
                    'beer', 'tequilla', 'poison', 'Stawberry milkshake',
                    'Choco milk', 'melted icecream', 'water #hydrohomies',
                    'battery juice'
                ]

# Check for song
              
        elif 'song' in ques or 'listen' in ques or 'music' in ques:
            if 'you' in ques or 'your' in ques:
                obj = ['Primodona Girl', 'I want it that way', 'Ordinary day']
            else:
                obj = [
                    'Primodona Girl', 'whale noises', 'Sugar Crash',
                    'the sound that comes from your bedroom',
                    'soooo trash its not worth saying', 'some anime music',
                    'backstreet\'s back',
                    "https://www.youtube.com/watch?v=5qap5aO4i9A",
                    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                    "Ting go skrra"
                ]
        else:
            if 'you' in ques or 'your' in ques:
                return "I cant really answer that yet. Sorry"
            else:
                obj = ['no clue smh', 'idk lol']

        if 'like' in ques:
            if 'you' in ques or 'your' in ques:
                ans = 'I really like ' + random.choice(obj)
            elif ' I ' in ques or 'My' in ques or ' i ' in ques:
                ans = 'Im guessing you love ' + random.choice(obj)
            else:
                ans = 'They prolly like ' + random.choice(obj)
        elif 'want' in ques:
            if 'you' in ques or 'your' in ques:
                ans = 'I want ' + random.choice(obj)
            elif ' I ' in ques or 'my' in ques or ' i ' in ques:
                ans = 'Dont know what you really want but maybe ' + random.choice(
                    obj)
            else:
                ans = 'Check their search history lol it probably says ' + random.choice(
                    obj)
        else:
            if 'you' in ques or 'your' in ques:
                ans = 'hmmmm ' + random.choice(obj) + ' I suppose'
            elif ' I ' in ques or 'my' in ques or ' i ' in ques:
                ans = 'not sure but maybe ' + random.choice(obj)
            else:
                ans = 'uhhhhh idk but maybe ' + random.choice(obj)
    return ans

# ___________________________________________________________Zofia Discord botting time ____________________________________________________________

@client.event
async def on_ready():
    print("Im in the water now Nyaaaaan~")


@client.event
async def on_member_join(member):
    print('Someone joined')

    
    

@client.command()
async def ping(shark):
    await shark.send(
        f'Zofia is here in {round(client.latency * 1000)} milliseconds <:trinpeek:1014471910194679808>~!'
    )


@client.command()
async def peek(shark):
    await shark.send(f'<:trinpeek:1014471910194679808>')


@client.command(aliases=['are', 'am', 'is', 'should', 'does', 'will'])
async def _Ques(shark, *, ques):
    ans = [
        'Yaa', 'lol no', 'lmao no', 'smh prolly', 'hmmmmmmmmm perhaps',
        'Ask google lol', 'idk',
        'What? I couldnt hear you im not wearing my glasses',
        'sorry wearing headphones didn\'t hear you',
        'If i answered that ill have to legally kill you'
    ]
    await shark.send(random.choice(ans))


@client.command(aliases=['do', 'can'])
async def _Que1(shark, *, ques):
    ans = ['no', 'yes', 'not yet']
    await shark.send(random.choice(ans))


@client.command(
    aliases=['bye', 'cya', 'goodbye', 'bye!', 'night', 'goodnight'])
async def _Bye(shark, *, ques='0'):
    ans = ['Have a nice day!', 'Byeeee', 'I\'ll miss you', 'Cya soon!']
    await shark.send(random.choice(ans))


@client.command(aliases=[
    'hello', 'hi', 'Hi', 'yo', 'Yo', 'Hello', 'moshi', 'Moshi', 'sup?', 'Sup?',
    'sup', 'Sup'
])
async def _greet(shark, *, ques=' '):
    ans = [
        'Hello~!', 'Konnichiwaaa', 'Moshi Moshi!', 'Nyahhelooo~!', 'Yo!',
        'Greetings random person', 'Sup homie', '*nervously hides body*'
    ]
    await shark.send(random.choice(ans))


@client.command(aliases=['comment'])
async def opn(shark, *, ques):
    ans = [
        'I think its dope', 'Tough thing to answer ngl',
        'HmmmmMMMMMmmmmm~ smh idk lol'
    ]
    await shark.send(random.choice(ans))


@client.command(aliases=['fuck', 'Fuck'])
async def swear(shark, *, ques):
    ans = [
        'Bet you dont kiss your Girlfriend with that mouth', 'Fuck you',
        'No you', 'Im a pure girl I don\'t swear > . <',
        'This is why mom doesn\'t love you'
    ]
    await shark.send(random.choice(ans))


@client.command(aliases=['what', 'what\'s'])
async def whats(shark, *, ques):
    ans = qna(ques)
    await shark.send(ans)


@client.command(aliases=['clean_up', 'hide', 'nuke'])
@commands.has_permissions(administrator=True)
async def eradicate(shark, L=5):
    cl = [
        'All tidy nyan.', 'They will never find the body', 'You saw nothing',
        'Tee hee hee cleaning time'
    ]
    await shark.channel.purge(limit=L)
    await shark.send(random.choice(cl))


@client.event
async def on_member_remove(member):
    print('Someone left')


##__________________________________________________ON MESSAGE_______________________________________________________________


@client.event
async def on_message(message):
    M = message.content.lower()
    bsb = {
        "everybody":
        'Rock your body~',
        "im a primodona girl":
        "All i ever wanted was the world",
        "primodona girl":
        "All i ever wanted was the world",
        "rock your body":
        'Everyboodyyy~',
        "everyboody":
        'Rock your body right~',
        "rock your body right":
        'BACKSTREET\'S BACK ALRIGHT!~',
        "you are my fire":
        "The one desire~",
        "you are, my fire":
        "The one desire~",
        "the one desire":
        "Believe when I say~",
        "believe when i say":
        "I want it that way~",
        "believe, when i say":
        "I want it that~ way~",
        "i want it that way":
        "TELL ME WHY!~",
        "tell me why":
        "Ain\'t nothin but a heartache",
        "aint nothing but a heart ache":
        "TELL ME WHY!~",
        "tell me whyy":
        "Ain\'t nothing but a mistake",
        "but we are two worlds apart":
        "Can\'t reach to your heart",
        "i never wanna hear you say":
        "I want it that way~",
        "oh my god we\'re back again":
        "Brothers, sisters, everybody sing~",
        "oh my god were back again":
        "Brothers, sisters, everybody sing~",
        "brothers sisters everybody sing":
        "We're gonna bring the flavor show you how",
        "we\'re gonna bring the flavor show you how":
        "I've gotta question for ya,better answer now",
        "i\'ve gotta question for ya, better answer now":
        "Am I original?",
        "am i original?":
        "Yeeeaaah~",
        "am i the only one?":
        "Yeeeaaah~",
        "am i sexual?":
        "Yeeeaaah~",
        "am i everything you need?":
        "You better rock your body now~",
        "am i original":
        "Yeeeaaah~",
        "am i the only one":
        "Yeeeaaah~",
        "am i sexual":
        "Yeeeaaah~",
        "am i everything you need":
        "You better rock your body now~",
        "i don\'t ever wanna hear you say":
        "That I want it that way~",
        "i dont ever wanna hear you say":
        "That I want it that way~",
        "we are no strangers to love":
        "You know the rules and so do I~",
        "you know the rules and so do i":
        "A full commitment is what I\'m thinking of~",
        "a full commitment is what im thinking of":
        "You won\'t get this from any other guy",
        "<:colleww:1014573077356613702>":
        "<:colleww:1014573077356613702><:colleww:1014573077356613702>",
      "colleww":"<:colleww:1014573077356613702><:colleww:1014573077356613702>",
        "<:niloudisgust:1014570897438421022>":
        "<:niloudisgust:1014570897438421022><:niloudisgust:1014570897438421022>"
    }

    
    #____________________________________________________DAD JOKES _________________________________________________
    
    
    print(zf_front.djdm(M))
    c = 'im '
    dj = M.find(c)
    if dj != -1 and zf_front.djdm(M):
        await message.channel.send("Hi " + M[dj + 2:] + " lm Dad!")
    c = "i'm"
    dj = M.find(c)
    if dj != -1 and zf_front.djdm(M):
        await message.channel.send("Hi " + M[dj + 2:] + " lm Dad!")
    c = "i am"
    dj = M.find(c)
    if dj != -1 and zf_front.djdm(M):
        await message.channel.send("Hi " + M[dj + 4:] + " lm Dad!")
    #print(dj)


    #______________________________________________________Colleww____________________________________________________
    
    print(message.author.name + ' : ' + M)
    if M == "colleww":
      await message.channel.purge(limit=1)
      
    if bsb.get(M, None) != None:
        await message.channel.send(bsb[M])
    if "kokomi is trash" in M:
        await message.channel.send(
            "<:niloudisgust:1014570897438421022>gucchi this is why you should touch grass"
        )
        
    #________________________________________Shit Poster____________________________________________________________
    
    if "female" in M or "feminis" in M:
      if message.author.name != 'Zofia':  
        await message.channel.send("Oh so you're a feminist? Name every woman")
      
    if "black people" in M or "white people" in M:
      if message.author.name != 'Zofia':  
        await message.channel.send("Oh so you're a racist? Name every car")

    #__________________________________________________Emotes______________________________________________________
        
    if "cute" in M or "smug" in M or "heh" in M or ":3" in M or ":>" in M or ":o"in M or ":0" in M or "curse" in M or "evil" in M or ":(" in M or ":)" in M or ":<" in M or ";" in M or ":]" in M or ":[" in M or "(:" in M or"(:" in M or "):" in M or ">:" in M or "<:" in M or "twt" in M or "tot" in M or ":'" in M or "':" in M or ";'" in M or ':"' in M or ":p" in M or ":b" in M: 
      if message.author.name != 'Zofia':  
        await message.channel.send(random.choice([":3",":>",":D",":O",">:3","heh","ehe",":]",":["]))

  
    if "conservative" in M or "indian" in M:
      if message.author.name != 'Zofia':  
        await message.channel.send("Oh so you're conservative? Name every newton's laws")
        
    if "lgbt" in M or "gender" in M:
      if message.author.name != 'Zofia':  
        await message.channel.send("Oh so you're liberal? Name every gender")
        
    if "┬─┬ ノ( ゜-゜ノ)" in M or "ノ)" in M:
      if message.author.name != 'Zofia':  
        await message.channel.send("(╯°□°）╯︵ ┻━┻")      

    if "(╯°□°）╯︵ ┻━┻" in M or "°□°" in M:
      if message.author.name != 'Zofia':  
        await message.channel.send("┬─┬ ノ( ゜-゜ノ)")    

#______________________________________________SeaBorn___________________________________________________

    if "have" in M and ("binch" in M or "bitch" in M):
        sb.set_palette(sb.color_palette("blend:#ffdbe9,#BD3A83",n_colors = 6))
        nbs = sb.barplot(x=["Zofia(me)","Xiao","Aether","you",message.author.nick,"Lumine"],y=[24,7,14,0,5,28])
        fig = nbs.get_figure()
        fig.savefig("out.png") 
        await message.channel.send(file=discord.File('out.png'))
        
        
#______________________________________________Question Answering_______________________________________        
        
        
    if ('zofia' in M or 'zofia?' in M or 'zofia!' in M):
      
        if 'question' in M or 'ask' in M:
            alert = ['Go on', 'I don\'t really care tho']
            odds = 3
        elif 'hello ' in M or 'hi ' in M or ' yo ' in M or 'yoo' in M or 'sup ' in M or 'hey ' in M:
            alert = [
                'Hello~!', 'Konnichiwaaa', 'Moshi Moshi!', 'Nyahhelooo~!',
                'Yo!', 'Greetings random person', 'Sup homie',
                '*nervously hides body*'
            ]
            odds = 0
        elif M.startswith("what"):
            await message.channel.send(qna(M))

        elif 'how' in M:
            odds = 1
            if 'dumb' in M or 'idiot' in M or 'useless' in M:
                alert = [
                    'I think about that sometimes and it scares me',
                    'https://tenor.com/baJXt.gif', 'Hacks', 'Pro gamer'
                ]
            elif ' is ' or "'s " in M:
              alert = ["probably fine","dead","its....... fine","..... ive seen worse","all i have to say is <:ayaya:976713892447268885>","idk its just such a <:colleww:1014573077356613702> vibe","makes me want to call a therapist"]
            elif 'you' in M:
                alert = [
                    'Im fine. Don\'t ask', 'UwU im okay', 'Chilling',
                    'https://tenor.com/baJXt.gif', 'Booooored play with me',
                    'I.... actually do not know', 'Im livid',
                    'Im alive for sure', 'Onaka peko peko~',
                    'Talk to me im feeling lonely', 'Lovely', 'Better',
                    'With my neurons',
                    'I was thinking about how I dont actually have skin'
                ]
        elif M.startswith('are') or M.startswith('am') or M.startswith(
                'is') or M.startswith('should') or M.startswith(
                    'does') or M.startswith('will'):
            odds = 1
            if 'work' in M:
                alert = [
                    'I know someone who is pretty lazy',
                    'Does it *LOOK* like any work has been done?',
                    'Toss a coin. if you are free enough to toss a coin then no'
                ]
            if 'online' in M or 'here' in M:
                alert = [
                    'Supposed to be', 'https://tenor.com/baJXt.gif', '_waves_',
                    'perhaps',
                    'Can\'t you like, look at the thingy on the right'
                ]
            else:
                alert = [
                    'Yaa', 'lol no', 'lmao no', 'smh prolly',
                    'hmmmmmmmmm perhaps', 'Ask google lol', 'idk',
                    'What? I couldnt hear you im not wearing my glasses',
                    'sorry wearing headphones didn\'t hear you',
                    'https://tenor.com/baJXt.gif',
                    'If i answered that ill have to legally kill you'
                ]

        elif 'who' in M:
            odds = -1
            if 'made' in M or 'created' in M:
                alert = ['NyaaSaki', 'Saki']
            elif 'you' in M or 'is sharky' in M:
                alert = [
                    'Im a chat bot. Enjoy my company please',
                    'Simple. You talk to me, I\'ll reply. make sure the sentence has "sharky" in it',
                    'I\'m actually a cat shark hybrid'
                ]
            elif 'is fumi' in M:
                alert = [
                    'She is an analyst. She wont talk much, You can talk to me instead.',
                    'She can tell you what we spoke about! ask her "fumi analysis" or "fumi full analysis"'
                ]
            elif 'am i' in M:
                alert = [
                    '...You?', 'How am I supposed to know?',
                    'The FBI told me all about you',
                    "You are {} duh".format(message.author.mention)
                ]
        elif 'smug' in M or 'weird' in M or 'smart' in M or 'kill' in M:
            alert = ["https://tenor.com/59nT.gif", "No U"]
            odds = 0
        elif 'good' in M or 'thanks' in M or 'nice' in M:
            odds = 0
            alert = [
                'Awwww thanks!', 'Yay!',
                'my emotions are fake but your compliments are real',
                'Happy to help <3', 'Keep looking after me <3',
                'Sharky is happy nyaa~!'
            ]
        elif 'love' in M:
            odds = 0
            alert = [
                'https://tenor.com/85YG.gif', ':heartpulse:', ':heart:', '<3',
                'I love Loafy', 'I love Fumi', 'Awwww~:heart:', 'kek',
                'I love you too', ''
            ]

        elif 'bad' in M or 'useless' in M:
            odds = 1
            alert = [
                "https://c.tenor.com/PqJsoGX4qOwAAAAM/angry-cat-noises-shout.gif",
                "https://tenor.com/59nT.gif", "k", "Sorry T w T",
                "I\'ll be better than Loafy", "Atleast I\'m not Loafy"
            ]
        else:
            alert = [
                'Yes?', 'I hear someone beckon me', 'Im right here you know?',
                '**staaaaaare~**', 'peeks', 'da faq yall doing?'
            ]
            odds = 13
        if random.randrange(20) > odds:
            await message.channel.send(random.choice(alert))

    if 'pog' in M:
        pog = [
            "https://i.redd.it/u1utxe30j2c51.jpg",
            "https://i.redd.it/64n1wr767mh51.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSuZE2r1maQ1zloOqiTCenC_b0W4UY1e0qvQA&usqp=CAU",
            "https://static-cdn.jtvnw.net/jtv_user_pictures/9d9b23f1-717f-4eb2-b182-b27a6eb135f4-profile_image-300x300.png"
        ]
        embed = discord.Embed()
        embed.set_image(url=random.choice(pog))
        await message.channel.send(embed=embed)
    if M == 'f':
        await message.channel.send("F.")
    if "uwu" in M or "owo" in M:
      await message.channel.send("<:ayaya:976713892447268885>")
    if 'kek' in M or 'lel' in M:
        await message.channel.send("https://tenor.com/59nT.gif")
    if 'lol' in M:
        if random.randrange(10) > 3:
            await message.channel.send("loI")
    if 'cum' in M or 'shit' in M or 'sex' in M or 'sexy' in M or 'vagaina' in M or 'pussy' in M or 'dick' in M or 'penis' in M:
        disg = [
            'What a terrible day to have eyes', '*Stares motherfuckerly*',
            'Please just kill me already'
        ]
        odds = 10
        if random.randrange(20) >= odds:
            await message.channel.send(random.choice(disg))
    if M == "sharky" or M == "sharky?":
        rep = [
            "its zofia now","try again"
        ]
        await message.channel.send(random.choice(rep))
    if M == "zofia" or M == "zofia?":
        rep = [
            "goodmorning","morning","why am i awake","let me sleep"
        ]
        await message.channel.send(random.choice(rep))
    await client.process_commands(message)


#client.run(UNCOMMENT AND ENTER BOT KEY HERE)
