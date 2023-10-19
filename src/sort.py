class Dinosaurs:
    def __init__(self, predators):
        self.predators = predators
    def __str__(self) -> str:
        return "this is the value {item}".format(item=self.predators)
    def sort(self, listOfDinosaurs)->[str]:
        returnValue = []
        for dinoInput in listOfDinosaurs:
            if self._isPredator(dinoInput)==False:
                returnValue.append(dinoInput)
        return returnValue
    def _isPredator(self,dinosaur)-> bool:
        for predator in self.predators:
            if predator == dinosaur:
                return True
        return False
