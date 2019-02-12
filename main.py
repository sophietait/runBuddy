import models
import pprint

run1 = models.runData('models/examples/run2.csv')
print(run1.getTotalDistance())
print(run1.getFastestSpeed())
print(run1.getLatLong())
