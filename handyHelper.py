from yamlcfg import YamlConfig
from subprocess import getoutput


class prePushTesting():
    """ runs sh camands on a local dev """

    def __init__(self, _runLinks=["python ", "pep8"]):
        self.config = YamlConfig(path='bitbucket-pipeline.yml')
        self.content = self.config.pipelines['default']
        self.safeCommands = _runLinks
        # print(self.content)

    def dictKeyExists(self, _obj={}, _key=''):
        try:
            a = _obj[_key]
            return True
        except Exception as e:
            return False

    def runCommands(self):
        # print(self.content)
        for e in self.content:
            if self.dictKeyExists(e, 'step'):
                if self.dictKeyExists(e['step'], 'script'):
                    for item in e['step']['script']:
                        for able in self.safeCommands:
                            if able in item:
                                print("running command - [{}]".format(item))
                                print(getoutput(item))
                else:
                    print('step-script dose not exist')
                    pass
            else:
                print('step dose not exist')
                pass
