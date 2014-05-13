# coding=utf-8
import praw, re, time, random
from pprint import pprint
r = praw.Reddit('User-Agent: bodybot/1.0 by heads_need_bodies')
r.login('username', 'password')

already_done = []
all_comments = r.get_comments('all')

intro = u'\u0020'u'\u0020'u'\u0020'u'\u0020'
new = u'\u0020'u'\u0020'+'\n'

head1 = u'ಠ_ಠ'.encode('utf-8')
head2 = u'° ͜ʖ ͡°'.encode('utf-8')
head3 = u'͠°͟ʖ͡°'.encode('utf-8')
head4 = u'ಥ_ಥ'.encode('utf-8')
head5 = u'ʘ‿ʘ'.encode('utf-8')
head6 = u'ಠ‿↼'.encode('utf-8')
head7 = u'(ツ)'.encode('utf-8')
head8 = u'(°_o)'.encode('utf-8')
head9 = u'(¬‿¬)'.encode('utf-8')
head10 = u'►_◄'.encode('utf-8')
head11 = u'ᶘ ᵒᴥᵒᶅ'.encode('utf-8')
head12 = u'°□°'.encode('utf-8')
head13 = '>_<'.encode('utf-8')
head14 = u'ʕ•ᴥ•ʔ'.encode('utf-8')
head15 = u'ﾟヮﾟ'.encode('utf-8')
head16 = u'ಠ╭╮ಠ'.encode('utf-8')
head17 = u'⌐■_■'.encode('utf-8')
head18 = u'•_•'.encode('utf-8')
head19 = u'◉ω◉'.encode('utf-8')
head20 = u'ﾟ∀ﾟ'.encode('utf-8')

heads = [head1, head2, head3, head4, head5, head6, head7, head8, head9, head10, head11, head12, head13, head14, head15, head16, head17, head18, head19, head20]
small_heads = [head1, head4, head5, head6, head7, head12, head13, head15, head16, head17, head18, head19, head20]

while True:
    all_comments = r.get_comments('Funny+AdviceAnimals+4ChanMeta')   
    for comment in all_comments:
        if not hasattr(comment, 'body'):
            continue
        else:
            if comment.author.name != 'heads_need_bodies' and comment.id not in already_done:
                already_done.append(comment.id)
                for head in heads:
                    if head in comment.body.encode('utf-8'):
                        if head in small_heads:
                            library = 'small_heads'
                        else:
                            library = 'large_heads'
                        head = head.decode('utf-8')
                        body1 = (intro+head+new+
                                 intro+' |'+new+
                                 intro+'/|\\'+new+
                                 intro+' |'+new+
                                 intro+' LL').encode('utf-8')

                        body2 = (intro+'|  o\\'+new+
                                 intro+'|W   \\'+head+new+
                                 intro+'|      |\\'+new+
                                 intro+'|     /-\\'+new+
                                 intro+'|   /     \\'+new+
                                 intro+'|'+new+
                                 intro+'|').encode('utf-8')

                        body3 = (intro+' '+head+new+
                                 intro+'/-|--/`'+new+
                                 intro+'\ |'+new+
                                 intro+'  /--i'+new+
                                 intro+' /   L'+new+
                                 intro+' L').encode('utf-8')

                        body4 = (intro+'   __'+head+new+
                                 intro+' _ \<_'+new+
                                 intro+'(_)/(_)').encode('utf-8')

                        body5 = (intro+head+new+
                                 intro+'/|\\'+new+
                                 intro+'(o-"='+new+
                                 intro+'/ \\').encode('utf-8')

                        body6 = (intro+'  '+head+'_/'+new+
                                 intro+' _/|'+new+
                                 intro+' __)\\'+new+
                                 intro+'`    \  o').encode('utf-8')

                        body7 = (intro+'       '+head+' ,    o__'+new+
                                 intro+'        [</     [\/'+new+
                                 intro+'    (`---/-------/----\')'+new+
                                 intro+'\~\~\~\~@\~\~\~\@~\~\~\~\~\~\~\~').encode('utf-8')

                        body8 = (intro+'        __'+new+
                                 intro+'       /  \\'+new+
                                 intro+'       \  /'+new+
                                 intro+'       /\/'+new+
                                 intro+'      /  %'+new+
                                 intro+'     /    %'+new+
                                 intro+head+' /'+new+
                                 intro+' |_/'+new+
                                 intro+'/|'+new+
                                 intro+'/ \\').encode('utf-8')        

                        body9 = (intro+head+'   ________________'+new+
                                 intro+'/\_  _|              |'+new+
                                 intro+'\__`[________________|'+new+
                                 intro+'] [\,/][           ][').encode('utf-8')

                        body10 = (intro+'     |'+new+
                                  intro+'   /   \\'+new+  
                                  intro+'  /     \\'+new+      
                                  intro+' (__'+head+'__)'+new+
                                  intro+'   |||||'+new+
                                  intro+'   |||||'+new+
                                  intro+'\_///| \\__/'+new+
                                  intro+' _// |  \_'+new+
                                  intro+'  / /').encode('utf-8')
                                  
                        body11 = (intro+'          .----.'+new+
                                  intro+' ____    __\\\\\\__'+new+
                                  intro+' \___\'--"         .-.'+new+
                                  intro+' /___<          \' '+head+'\''+new+
                                  intro+'/____,--.       y   B'+new+
                                  intro+'        "".____  _-"'+new+
                                  intro+'        //    / /'+new+
                                  intro+'              ]/').encode('utf-8')

                        body12 = (intro+'\   '+head+'   /'+new+
                                  intro+' \ __|__ /'+new+
                                  intro+'  [____]]'+new+ 
                                  intro+'   __|__'+new+ 
                                  intro+'  /    /\\'+new+  
                                  intro+' /    /  \\'+new+
                                  intro+'(____(____)').encode('utf-8')

                        body13 = (intro+' O'+new+    
                                  intro+'/\__'+head+new+
                                  intro+'> > \\').encode('utf-8')

                        body14 = (intro+head+new+
                                  intro+'<|>'+new+
                                  intro+'/'+u'ω'+'\\').encode('utf-8')

                        body15 = (intro+' (\ /)'+new+
                                  intro+' ('+head+')'+new+
                                  intro+' '+u'ᑕ'+'( )'+u'ᑐ'+new+
                                  intro+'(") (")').encode('utf-8')

                        body16 = (intro+'  _'+new+
                                  intro+'_|_|_'+new+
                                  intro+'{'+head+'}'+new+
                                  intro+'/|O|\\'+new+
                                  intro+'\[|]/'+new+
                                  intro+' / \\'+new+
                                  intro+' | |'+new+
                                  intro+'_| |_').encode('utf-8')

                        body17 = (intro+'___    _________________________________________'+new+
                                  intro+'|  |==|  |     |                                 \\'+new+
                                  intro+'|  ||||  |+---+|+-----+-----+-----+-----+   +-----\\'+new+
                                  intro+'|  ||||  ||   |||     |     |     |     |   |  '+head+' \\'+new+
                                  intro+'|  ||||  ||   |||_____|_____|_____|_____|   |_/|o|\_\\'+new+
                                  intro+'|  ||||  ||___||===== heads_need_bodies Express =====\\'+new+
                                  intro+'|__|==|__|_____|_____________________________________|[}'+new+
                                  intro+'         ( O O )                           ( O O )'+new+
                                  intro+'==============================================================').encode('utf-8')

                
                        if library == 'small_heads':
                            bodies = [body1, body2, body3, body4, body5, body6, body7, body8, body9, body10, body11, body12, body13, body14, body15, body16, body17, body18]
                        else:
                            bodies = [body1, body2, body3, body4, body5, body6, body7, body8, body9, body11, body13, body14, body15]
                        
                        hotshotjosh = [body10, body11]
                        scored420yearsago = [body12]
                        chbay = [body14]
                        happyfacekillah = [body15]
                        tyx = [body16]
                        ChromeLynx = [body17]
                        bod = random.choice(bodies)
                        if bod in hotshotjosh:
                            credit = ('\n\n'+'Credit to /u/hotshotjosh for sending me this body.')
                        elif bod in scored420yearsago:
                            credit = ('\n\n'+'Credit to /u/scored420yearsago for sending me this body.')
                        elif bod in chbay:
                            credit = ('\n\n'+'Credit to /u/chbay for sending me this body.')
                        elif bod in happyfacekillah:
                            credit = ('\n\n'+'Credit to /u/happyfacekillah for sending me this body.')
                        elif bod in tyx:
                            credit = ('\n\n'+'Credit to /u/Tyx for sending me this body.')
                        elif bod in ChromeLynx:
                            credit = ('\n\n'+'Credit to /u/ChromeLynx for sending me this body.')
                        else:
                            credit = ('')
                        comment.reply(bod+credit+'\n\n')
                        print comment.id
                    






#body1
#ಠ_ಠ
# |
#/|\
# |
# LL

#body2
#|  o\
#|W   \ಠ_ಠ
#|      |\
#|     /-\
#|   /     \
#|
#|

#body3
# ಠ_ಠ
#/-|--/`
#\ |
#  /--i
# /   L
# L

#body4
#   __ಠ_ಠ
# _ \<_
#(_)/(_)

#body5
#ಠ_ಠ
#/|\
#(o-"=
#/ \

#body6
#  ಠ_ಠ_/
# _/|
# __)\
#`    \  o

#body7
#       ಠ_ಠ,     o__
#        [</     [\/
#    (`---/-------/----')
#\~\~\~@\~\~\~\~@\~\~\~\~\~\~\~\~

#body8
#        __
#       /  \
#       \  /
#       /\/
#      /  %
#     /    %
#ಠ_ಠ / 
# |_/
#/|
#/ \        

#body9
#ಠ_ಠ   ________________
#/\_  _|              |
#\__`[________________|
#] [\,/][           ][

#body10
#     |
#   /   \       
#  /     \      
# (__ಠ_ಠ__)
#   |||||
#   |||||
#\_///| \\__/
# _// |  \_
#  / /
          
#body11
#          .----.
# ____    __\\\\\\__
# \___'--"         .-.
# /___<          ' ಠ_ಠ'
#/____,--.       y   B
#        "".____  _-"
#        //    / /
#              ]/

#body12
#\   ಠᴗಠ   /
# \ __|__ /
#  [____]]  
#   __|__  
#  /    /\  
# /    /  \  
#(____(____)

#body13
# O    
#/\__O
#> > \

#body14
#ಠ_ಠ
#<|>
#/ω\

#body15
# (\ /)
# (ಠ_ಠ)
# ᑕ( )ᑐ
#(") (")

#body16
#  _
#_|_|_
#{ಠ_ಠ}
#/|O|\
#\[|]/
# / \
# | |
#_| |_

#body17
#             
#___    _________________________________________
#|  |==|  |     |                                 \
#|  ||||  |+---+|+-----+-----+-----+-----+   +-----\
#|  ||||  ||   |||     |     |     |     |   |  ಠ_ಠ \
#|  ||||  ||   |||_____|_____|_____|_____|   |_/|o|\_\
#|  ||||  ||___||===== heads_need_bodies Express =====\
#|__|==|__|_____|_____________________________________|[}
#         ( O O )                           ( O O )
#==============================================================
#*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *
                        

