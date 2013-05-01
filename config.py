import supybot.conf as conf
import supybot.registry as registry

def configure(advanced):
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('supybugz', True)

supybugz = conf.registerPlugin('supybugz')
conf.registerChannelValue(supybugz,'enable',registry.Boolean('False',"""Enable displaying messages from supybugz in channel?"""))

