from detecto import core, utils, visualize


dataset = core.Dataset('cards/')
model = core.Model(['poptag', 'speed', 'overlay'])

model.fit(dataset)