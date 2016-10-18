from collections import defaultdict
import json

tree = lambda: defaultdict(tree)

r = tree()

r['a']['b']='bb'
r['a']['c']['d']='dddd'

print json.dumps(r)
#{"a": {"c": {"d": "dddd"}, "b": "bb"}}

print r['a']['b']
#bb

print r['a']['c']['d']
#dddd
