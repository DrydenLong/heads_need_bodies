# coding=utf-8
import praw, re, time, random
from pprint import pprint
r = praw.Reddit('User-Agent: bodybot/1.0 by heads_need_bodies')
r.login('username', 'password')

already_done = []
all_comments = r.get_comments('all')

#Here we define the "spaces" to shorten the code of the bodies

sp = u'\xa0'
sp2 = u'\xa0'u'\xa0'
sp3 = u'\xa0'u'\xa0'u'\xa0'
sp4 = u'\xa0'u'\xa0'u'\xa0'u'\xa0'
sp5 = u'\xa0'u'\xa0'u'\xa0'u'\xa0'u'\xa0'
hair = u'\u200A'
thin = u'\u2009'
intro = u'\u0020'u'\u0020'u'\u0020'u'\u0020'
new = u'\u0020'u'\u0020'+'\n'


#All the heads/faces we am looking for

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

#Some heads just don't work with some body types, so we create 2 lists

heads = [head1, head2, head3, head4, head5, head6, head7, head8, head9, head10, head11, head12, head13, head14, head15, head16, head17, head18, head19]
small_heads = [head1, head4, head5, head6, head7, head12, head13, head15, head16, head17, head18, head19]

while True:
    all_comments = r.get_comments('Funny+Pics+AdviceAnimals')   
    for comment in all_comments:
        if not hasattr(comment, 'body'):
            continue
        else:
            if comment.author.name != 'heads_need_bodies' and comment.id not in already_done:
                already_done.append(comment.id)
                for head in heads:
                    if head in comment.body.encode('utf-8'):
                        if head in small_heads:
                            library = 'all_bodies'
                        else:
                            library = 'large_heads'
                        head = head.decode('utf-8')
                        body1 = (intro+head+new+
                                 intro+sp+'| '+new+
                                 intro+'/|\ '+new+
                                 intro+sp+'| '+new+
                                 intro+sp+'LL').encode('utf-8')
                        body2 = (intro+'|'+sp3+'o\\ '+new+
                                 intro+'|'+sp+'W'+sp3+'\\'+head+new+
                                 intro+'|'+sp5+sp2+'|\\ '+new+
                                 intro+'|'+sp5+sp+'/-\\ '+new+
                                 intro+'|'+sp4+'/'+sp5+'\\ '+new+
                                 intro+'|'+new+
                                 intro+'|').encode('utf-8')
                        body3 = (intro+sp+head+new+
                                 intro+'/-|--/`'+new+
                                 intro+'\\'+sp+'|'+new+
                                 intro+sp2+'/--i'+new+
                                 intro+sp+'/'+sp3+'L'+new+
                                 intro+sp+'L').encode('utf-8')
                        body4 = (intro+sp3+'__'+head+new+
                                 intro+sp+'_'+sp+'\<_'+new+
                                 intro+'(_)/(_)').encode('utf-8')
                        body5 = (intro+head+new+
                                 intro+'/|\\'+new+
                                 intro+'(o-"='+new+
                                 intro+'/'+sp+'\\').encode('utf-8')
                        body6 = (intro+sp2+head+'_/'+new+
                                 intro+sp+'_/|'+new+
                                 intro+sp+'__)\\'+new+
                                 intro+'`'+sp4+'\\'+sp3+'o').encode('utf-8')
                        body7 = (intro+sp5+sp4+head+sp+','+sp5+'o__,'+new+
                                 intro+sp5+sp5+'[</'+sp5+sp+'[\/'+new+
                                 intro+sp5+'(`\---/--------/----\')'+new+
                                 intro+'\~\~\~\~\~@\~\~\~\~@\~\~\~\~\~\~\~\~').encode('utf-8')
                        body8 = (intro+sp5+sp3+thin+'__'+new+
                                 intro+sp5+sp2+thin+'/'+sp2+'\\'+new+
                                 intro+sp5+sp2+thin+'\\'+sp2+'/'+new+
                                 intro+sp5+sp2+thin+'/\/'+new+
                                 intro+sp5+sp+thin+'/'+sp2+'%'+new+
                                 intro+sp5+thin+'/'+sp5+'%'+new+
                                 intro+head+sp+'/'+new+
                                 intro+sp+'|_/'+new+
                                 intro+'/|'+new+
                                 intro+'/'+sp+'\\').encode('utf-8')
                        body9 = (intro+head+sp4+'________________'+new+
                                intro+'/\_'+sp2+'_|'+sp5+sp5+sp5+sp+'|'+new+
                                intro+'\__`[__________________|'+new+
                                intro+']'+sp+'[\,/]['+sp5+sp5+sp3+'][').encode('utf-8')
                        body10 = (intro+sp5+sp+'|'+new+
                                  intro+sp4+hair+'/'+sp3+'\\'+new+
                                  intro+sp3+thin+'/'+sp5+'\\'+new+
                                  intro+sp2+'(__'+head+'__)'+new+
                                  intro+sp4+'|||||'+new+
                                  intro+sp4+'|||||'+new+
                                  intro+sp+'\_///|'+sp+'\\__/'+new+
                                  intro+sp2+'_//'+sp+'|'+sp2+'\_'+new+
                                  intro+sp2+'/'+sp2+'/').encode('utf-8')
                        body11 = (intro+sp5+sp5+'.----.'+new+
                                  intro+sp+'____'+sp4+'__\\\\\\\\\\\\__'+new+
                                  intro+sp+'\___\'--"'+sp5+sp4+'.-.\\'+new+
                                  intro+sp+'/___<'+sp5+sp5+'\''+sp+head+'\''+new+
                                  intro+'/____,--.'+sp5+sp2+'y'+sp4+'/'+new+
                                  intro+sp5+sp3+'"".____'+sp2+'_-"'+new+
                                  intro+sp5+sp3+'//'+sp4+'/'+sp+'/'+new+
                                  intro+sp5+sp5+sp4+']/').encode('utf-8')
                        body12 = (intro+sp+'\\'+sp3+head+sp3+'/'+new+
                                  intro+sp2+'\\'+sp+'__|__'+sp+'/'+new+
                                  intro+sp3+'[____]]'+new+
                                  intro+sp4+'__|___'+new+
                                  intro+sp3+'/'+sp4+'/\\'+new+
                                  intro+sp2+'/'+sp4+'/'+sp2+'\\'+new+
                                  intro+sp+'(____(____)').encode('utf-8')
                        body13 = (intro+sp+'O'+new+
                                  intro+'/\\'+sp+'__'+head+new+
                                  intro+'\|`>'+sp2+'\\').encode('utf-8')
                        body14 = (intro+head+new+
                                  intro+'<|>'+new+
                                  intro+'/'+u'ω'+'\\').encode('utf-8')
                        body15 = (intro+sp+'(\\'+sp+'/)'+new+
                                  intro+sp+'('+head+')'+new+
                                  intro+thin+thin+u'ᑕ'+'('+sp2+')'+u'ᑐ'+new+
                                  intro+thin+'(")'+sp+'(")').encode('utf-8')
                        body16 = (intro+sp2+'_'+new+
                                  intro+'_|_|_'+new+
                                  intro+'{'+head+'}'+new+
                                  intro+'/|O|\\'+new+
                                  intro+'\\'+hair+'[|]'+hair+'/'+new+
                                  intro+sp+'/'+sp+'\\'+new+
                                  intro+sp+'|'+sp+'|'+new+
                                  intro+'_|'+sp+'|_').encode('utf-8')
                                  
                        body17 = ("""\
                        
                                           ._ o o
                                           \_`-)|_
                                        ,""       \ 
                                      ,"  ## |   ಠ ಠ. 
                                    ," ##   ,-\__    `.
                                  ,"       /     `--._;)
                                ,"     ## /
                              ,"   ##    /
                        
                        
                        """).encode('utf-8')

                        if library == 'all_bodies':
                            bodies = [body1, body2, body3, body4, body5, body6, body7, body8, body9, body10, body11, body12, body13, body14, body15, body16, body17]
                        else:
                            bodies = [body1, body2, body3, body4, body5, body6, body7, body8, body9, body11, body13, body14, body15, body17]
                        
                        #Several Reddit users have sent in bodies to use, here we give them credit
                        hotshotjosh = [body10, body11]
                        scored420yearsago = [body12]
                        chbay = [body14]
                        happyfacekillah = [body15]
                        tyx = [body16]
                        bod = random.choice(bodies)
                        if bod in hotshotjosh:
                            credit = ('\n\n'+'Credit to /u/hotshotjosh for sending me this body.')
                        elif bod in scored420yearsago:
                            credit = ('\n\n'+'Credit to /u/scored420yearsago for sending me this body.')
                        elif bod in chbay:
                            credit = ('\n\n'+'Credit to /u/chbay for sending me this body.')
                        elif bod in happyfacekillah:
                            credit = ('\n\n'+'Credit to /u/happyfacekillah for sending me this body.')
                        if bod in tyx:
                            credit = ('\n\n'+'Credit to /u/Tyx for sending me this body.')
                        else:
                            credit = ('')
                        comment.reply(bod+credit+'\n\n')
                        print comment.id
