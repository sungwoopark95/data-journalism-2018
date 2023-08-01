class Mood(object):

    GENERIC = 1
    HIGH_TEMP = 2
    LOW_TEMP = 3
    STILL_COLD = 4
    HIGH_DUST = 5
    LOW_DUST = 6
    DUST_GOOD = 7

    def decision_temp(self, data):
        temp = float(data)

        if temp < 0:
            return self.LOW_TEMP

        if temp > 30:
            return self.HIGH_TEMP

        if (0<= temp <=15):
            return self.STILL_COLD

        if (15< temp <=30):
            return self.GENERIC

    def decision_dust(self, data):
        dust = float(data)

        if 80 <= dust < 200:
            return self.LOW_DUST

        if dust >= 200:
            return self.HIGH_DUST

        if dust < 80:
            return self.DUST_GOOD


