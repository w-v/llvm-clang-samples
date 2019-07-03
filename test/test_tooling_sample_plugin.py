import sys, unittest
from tools import SamplesTestCase

OUTPUT_HELLO_FUNCS = '''\
Hello: mult
Hello: fact
'''

class TestToolingSamplePlugin(SamplesTestCase):
    def test_hello_on_fact(self):
        self.assertOptPluginOutput('tooling_sample_plugin.so', [], 'funcallsample.cpp',
            OUTPUT_HELLO_FUNCS)

if __name__ == '__main__':
    unittest.main()
