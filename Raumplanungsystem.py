from random import *
class Raum:
    def __init__(self, __Fläche):
        self.Fläche=__Fläche

    def GetFläche (self):
        return self.Fläche
    def CalcMiete (self):
        return self.Fläche*10



    def __str__(self):
        return f"Fläche {self.Fläche} m² "

#raum1 = Raum (15)
#raum2 = Raum (100)
#print (raum1)
#print (raum2)
#print (f'Raum 1: {raum1.GetFläche()}, Miete: {raum1.CalcMiete()} €')
#print (f'Raum 2: {raum2.GetFläche()}, Miete: {raum2.CalcMiete()} €')

class Seminarraum(Raum):
    def __init__ (self,Fläche,__Plätze):
        super().__init__(Fläche)
        self.Plätze=__Plätze

    def SetPlätze(self,Plätze):
        self.Plätze = Plätze


    def GetPlätze (self):
        return self.Plätze

    def CalcMiete (self):
        return self.Fläche*8


    def __str__(self):
        return   super().__str__() + f"Plätze {self.Plätze}"

#seminar1 = Seminarraum (100, 40)
#print (seminar1)
#seminar2 = Seminarraum (200, 70)
#print (seminar2)
#seminar1.SetPlätze (50)
#print (f'Plätze 1: {seminar1.GetPlätze()}, Miete: {seminar1.CalcMiete()} €')
#print (f'Plätze 2: {seminar2.GetPlätze()}, Miete: {seminar2.CalcMiete()} €')

class Büro(Raum):

    def __init__(self,Fläche):
     super().__init__(Fläche)
     self.Namensliste = []

    def AddName(self,Name):
        self.Name=Name
        self.Name = self.Name.title()

        return self.Namensliste.append(self.Name)



    def SubName(self,Name):
        self.Name=Name
        self.Namensliste.remove(self.Name)




    def CalcMiete (self):
      return 100

    def __str__(self):
        return   super().__str__() + f"Mitarbeiter : {self.Namensliste}"

#büro1 = Büro (30)
#büro2 = Büro (40)
#büro1.AddName ('Roger Rabbit')
#büro1.AddName ('Yosemite Sam Elmer Fudd')
#büro2.AddName ('  pinky   brain')
#büro2.AddName ('Wile Coyote')
#büro2.AddName ('Speedy Gonzales')
#print (büro1)
#print (büro2)
#büro2.SubName ('Wile Coyote')
#print (büro2)
#print (f'Miete Büro 1: {büro1.CalcMiete()}')

class Raumverwaltung:
    def __init__(self):
        self.__FB1RaumTabelle={}
        self.__FB2RaumTabelle = {}
        self.Raumnummer=100

    def AddRaum(self,FB,Raum):
        self.FB=FB
        self.Raum=Raum


        if FB==1:
            self.__FB1RaumTabelle[self.Raumnummer] = Raum
        elif FB == 2:
            self.__FB2RaumTabelle[self.Raumnummer] = Raum
        else:
            return "Error"
        self.Raumnummer+=1

        return self.Raumnummer-1

    def PrintRäume(self):
        for keys,values in self.__FB1RaumTabelle.items():
            print(f"FB1 Raumnummer{keys} {values}")
        for keys, values in self.__FB2RaumTabelle.items():
            print(f"FB2 Raumnummer{keys} {values}" )

    def Umwidmung(self,Raumnummer):

        if Raumnummer in self.__FB1RaumTabelle:
           room=self.__FB1RaumTabelle[Raumnummer]
           del self.__FB1RaumTabelle[Raumnummer]
           self.__FB2RaumTabelle[Raumnummer]=room
           #return self.__FB2RaumTabelle[Raumnummer]

        elif Raumnummer in self.__FB2RaumTabelle:
            room = self.__FB2RaumTabelle[Raumnummer]
            del self.__FB2RaumTabelle[Raumnummer]
            self.__FB1RaumTabelle[Raumnummer]=room

            #return self.__FB1RaumTabelle[Raumnummer]


    def CalcMiete(self,FB):
        x=0

        if FB==1:
            for key,values in self.__FB1RaumTabelle.items():
              x += values.CalcMiete()
            return x
        if FB == 2:
            for key, values in self.__FB2RaumTabelle.items():
                x += values.CalcMiete()
            return x


seminar1 = Seminarraum (100, 40)
seminar2 = Seminarraum (200, 70)
büro1 = Büro (30)
büro2 = Büro (40)
büro1.AddName ('Elmer Fudd')
büro2.AddName ('Wile Coyote')
büro2.AddName ('Speedy Gonzales')
manager = Raumverwaltung ()
s1 = manager.AddRaum (1, seminar1)
s2 = manager.AddRaum (2, seminar2)
b1 = manager.AddRaum (1, büro1)
b2 = manager.AddRaum (1, büro2)
manager.PrintRäume ()
manager.Umwidmung (b2)
manager.PrintRäume ()
print (f'Miete FB1: {manager.CalcMiete (1)} €')
print (f'Miete FB2: {manager.CalcMiete (3)} €')
