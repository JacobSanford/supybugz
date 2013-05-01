import re
import requests
import supybot.callbacks as callbacks
import supybot.ircutils as ircutils
import supybot.ircmsgs as ircmsgs
from supybot.commands import *
from fogbugz import FogBugz
import fbSettings

class supybugz(callbacks.Plugin):
    """Add the help for "@plugin help supybugz" here
    This should describe *how* to use this plugin."""
    threaded = True

    def doPrivmsg(self, irc, msg):
        if(self.registryValue('enable', msg.args[0])):
            match = re.search('.*Bug[sz]id *: *(\d{1,5})', msg.args[1], re.IGNORECASE)
            if match:
                fb = FogBugz(fbSettings.fb_url)
                fb.logon(fbSettings.fb_user, fbSettings.fb_pass)
                resp = fb.search(q=match.group(1),cols='sTitle,sStatus,sPriority')
                if len(resp.findAll('case')) > 0 :
                    for cur_case in resp.cases.childGenerator():
                        title_message = '[BugzID ' + match.group(1) + '] ' + ircutils.bold(str(cur_case.stitle.string).replace('<![CDATA[','').replace(']]>','')) + ' (' + cur_case.sstatus.string  + ', ' + cur_case.spriority.string  +')'
                        irc.queueMsg(ircmsgs.privmsg(msg.args[0], title_message))
                        url_message = fbSettings.fb_url + '/default.asp?' + match.group(1)
                        irc.queueMsg(ircmsgs.privmsg(msg.args[0], url_message))
                else :
                    irc.queueMsg(ircmsgs.privmsg(msg.args[0], 'Sorry, ' + ircutils.bold(match.group(1))  + ' is not a known BugID.'))

Class = supybugz

