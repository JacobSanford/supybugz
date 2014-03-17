import supybot.conf as conf
import supybot.registry as registry

def configure(advanced):
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('SupyBugz', True)

SupyBugz = conf.registerPlugin('SupyBugz')
conf.registerChannelValue(SupyBugz,'enable',registry.Boolean('False',"""Enable displaying messages from SupyBugz in channel?"""))

