import fractions

class Fushu: 
    def __init__(self, shibu=fractions.Fraction(0), xubu=fractions.Fraction(0)): 
        self.shibu = shibu
        self.xubu = xubu

    # S. (1.1)
    def __add__(self, b): 
        return Fushu(self.shibu + b.shibu, self.xubu + b.xubu)

    # S. (1.2)
    def __mul__(self, b): 
        return Fushu(
                self.shibu * b.shibu - self.xubu * b.xubu, 
                self.shibu * b.xubu + self.xubu * b.shibu
                )

    # S. (1.3)
    @property
    def re(self): 
        return self.shibu

    @property
    def im(self): 
        return self.xubu

    # S. (1.4)
    def __sub__(self, b): 
        return Fushu(self.shibu - b.shibu, self.xubu - b.xubu)


    def __str__(self): 
        return '{} + {}i'.format(self.shibu, self.xubu)


if __name__ == '__main__': 
    print(Fushu(1, 2) - Fushu(2, 1))
